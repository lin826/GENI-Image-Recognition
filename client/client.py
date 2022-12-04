from fetchImg import *
import requests
import argparse

imageFolder = "image"

url = 'http://127.0.0.1:5000/recognize'


def parseOption():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--server", type=str, required=True, help="server address")
    parser.add_argument("-n", "--num", type=int, help="number of image", default=5)
    args = parser.parse_args()
    return args.server, args.num


if __name__ == '__main__':
    server, numOfImage = parseOption()
    # images = fetchImages(imageFolder, numOfImage)
    
    for i in range(numOfImage):
        # images[i].show()

        try:
            my_img = {'image': open(f"{imageFolder}/{i+1}.png", 'rb')}
            print("image fetch from local")
        except:
            fetchFromURL(imageFolder, str(i+1))
            my_img = {'image': open(f"{imageFolder}/{i+1}.png", 'rb')}
            print("image fetch from url")
        
        try:
            r = requests.post(server + "/recognize", files=my_img, timeout=200)
            print(r.json())
        except Exception as e:
            print(e)
            

        
        # convert server response into JSON format.
        

