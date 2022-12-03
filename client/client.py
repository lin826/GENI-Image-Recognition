from fetchImg import *
import requests

numOfImage = 5

images = []

imageFolder = "client/image"


if __name__ == '__main__':
    images = fetchImages(numOfImage)

    url = 'http://127.0.0.1:5000/recognize'
    for i in range(numOfImage):
        # images[i].show()

        my_img = {'image': open(f"{imageFolder}/{i+1}.png", 'rb')}
        r = requests.post(url, files=my_img)

        # convert server response into JSON format.
        print(r.json())

