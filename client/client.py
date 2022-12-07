from fetchImg import *
from output import *
from record import *
import requests
import argparse
import os
import shutil
from datetime import datetime

imageFolder = "image"
resultFolder = "result"

recordList = []

def parseOption():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--server", type=str, help="server address", default="http://server")
    parser.add_argument("-p", "--port", type=int, help="server address", default=5000)
    parser.add_argument("-n", "--num", type=int, help="number of image", default=5)
    parser.add_argument("-f", "--fetch", type=str, help="fetch the image from url with specific size width/height")
    parser.add_argument("-t", "--timeout", type=int, help="timeout", default=1000)
    args = parser.parse_args()
    return args.server, args.port, args.num, args.fetch, args.timeout


def checkFolder():
    try:
        os.mkdir(imageFolder)
    except:
        pass
    try:
        os.mkdir(resultFolder)
    except:
        pass


if __name__ == '__main__':
    server, port, numOfImage, fetchWidthHeight, timeout = parseOption()

    checkFolder()

    sumRTT = 0
    success = 0
    
    for i in range(numOfImage):

        fetchImage(imageFolder, i, fetchWidthHeight)
        
        requestTime = datetime.now().strftime("%H:%M:%S")
        try:
            my_img = {'image': open(f"{imageFolder}/{i+1}.png", 'rb')}
            url = server + ":" + str(port) + "/recognize"
            print("Waiting for server response...")
            r = requests.post(url, files=my_img, timeout=timeout)
            print("Results: ", end = "")
            if r.status_code == 200:
                success += 1
                result = r.json()
                print(result)
                shutil.copy(f"{imageFolder}/{i+1}.png", f"{resultFolder}/{i+1}.png")
                os.rename(f"{resultFolder}/{i+1}.png", f"{resultFolder}/{requestTime}_{result['text']}.png")
                # record
                responseTime = datetime.now().strftime("%H:%M:%S")
                width, height = parseWidthHeight(fetchWidthHeight)
                delta = datetime.strptime(responseTime, "%H:%M:%S") - datetime.strptime(requestTime, "%H:%M:%S")
                sumRTT += delta.total_seconds()
                record = Record(f"{imageFolder}/{i+1}.png", requestTime, responseTime, delta.total_seconds(), width, height)
                recordList.append(record)
            elif r.status_code >= 500 and r.status_code < 600:
                print("Server Error! " + r.content)
        except Exception as e:
            print(e)
        print()
    
    print(f"Send {numOfImage} requests, {success} success, {numOfImage-success} fail.")
    if numOfImage-success != numOfImage:
        print(f"Avareage RTT: {sumRTT/success}sec.")
    
    if recordList:
        outputCSV(datetime.now().strftime("%H:%M:%S"), recordList)

