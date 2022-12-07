from fetchImg import *
import requests
import argparse
import os
import shutil
from datetime import datetime

imageFolder = "image"
resultFolder = "result"


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
    
    for i in range(numOfImage):

        fetchImage(imageFolder, i, fetchWidthHeight)
        
        try:
            my_img = {'image': open(f"{imageFolder}/{i+1}.png", 'rb')}
            url = server + ":" + str(port) + "/recognize"
            print("Waiting for server response...")
            requestTime = datetime.now().strftime("%H:%M:%S")
            r = requests.post(url, files=my_img, timeout=timeout)
            responseTime = datetime.now().strftime("%H:%M:%S")
            # print(requestTime, responseTime)
            print("Results: ", end = "")
            if r.status_code == 200:
                result = r.json()
                print(result)
                shutil.copy(f"{imageFolder}/{i+1}.png", f"{resultFolder}/{i+1}.png")
                os.rename(f"{resultFolder}/{i+1}.png", f"{resultFolder}/{responseTime}_{result['text']}.png")
            elif r.status_code >= 500 and r.status_code < 600:
                print("Server Error! " + r.content)
        except Exception as e:
            print(e)
        print()

