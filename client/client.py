from fetchImg import *
import requests

numOfImage = 5

imageFolder = "image"

url = 'http://127.0.0.1:5000/recognize'


if __name__ == '__main__':
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

        r = requests.post(url, files=my_img)
        # convert server response into JSON format.
        print(r.json())

