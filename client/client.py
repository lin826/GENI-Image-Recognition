from fetchImg import *
import requests
import argparse
import os

imageFolder = "image"

url = 'http://127.0.0.1:5000/recognize'

defaultWidthHeight = "640/360"


def parseOption():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--server", type=str, required=True, help="server address")
    parser.add_argument("-n", "--num", type=int, help="number of image", default=5)
    parser.add_argument("-f", "--fetch", type=str, help="fetch the image from url with specific size width/height")
    args = parser.parse_args()
    return args.server, args.num, args.fetch


if __name__ == '__main__':
    server, numOfImage, fetchWidthHeight = parseOption()
    # images = fetchImages(defaultWidthHeight, imageFolder, numOfImage)

    try:
        os.mkdir(imageFolder)
    except:
        pass
    
    for i in range(numOfImage):
        # images[i].show()

        if fetchWidthHeight:
            fetchFromURL(fetchWidthHeight, imageFolder, str(i+1))
            print("image fetch from url")
        else:
            try:
                open(f"{imageFolder}/{i+1}.png")
                print("image fetch from local")
            except:
                fetchFromURL(defaultWidthHeight, imageFolder, str(i+1))
                print("image fetch from url")
        
        try:
            my_img = {'image': open(f"{imageFolder}/{i+1}.png", 'rb')}
            r = requests.post(server + "/recognize", files=my_img, timeout=200)
            print(r.json())
        except Exception as e:
            print(e)

