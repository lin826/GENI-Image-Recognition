import requests
from PIL import Image

imageFolder = "client/image"


def fetchFromURL(filename):
    img_url = "https://picsum.photos/640/360"

    # request image from url
    img = Image.open(requests.get(img_url, stream = True).raw)

    # save the imgage in the folder
    img.save(f"{imageFolder}/{filename}.png")

    # return img


def fetchFromLocal(num):
    img = Image.open(f"{imageFolder}/{num}.png")
    return img



def fetchImages(num):
    images = []
    for i in range(num):
        try:
            images.append(fetchFromLocal(str(i+1)))
            print("image fetch from local")
        except:
            fetchFromURL(str(i+1))
            images.append(fetchFromLocal(str(i+1)))
            print("image fetch from url")
    return images