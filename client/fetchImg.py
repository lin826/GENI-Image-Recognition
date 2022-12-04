import requests
from PIL import Image


def fetchFromURL(fetchWidthHeight, imageFolder, num):
    
    img_url = f"https://picsum.photos/{fetchWidthHeight}"

    # request image from url
    img = Image.open(requests.get(img_url, stream = True).raw)

    # save the imgage in the folder
    img.save(f"{imageFolder}/{num}.png")

    # return img


def fetchFromLocal(imageFolder, num):
    img = Image.open(f"{imageFolder}/{num}.png")
    return img



def fetchImages(fetchWidthHeight, imageFolder, num):
    images = []
    for i in range(num):
        try:
            images.append(fetchFromLocal(imageFolder, str(i+1)))
            print("image fetch from local")
        except:
            fetchFromURL(fetchWidthHeight, imageFolder, str(i+1))
            images.append(fetchFromLocal(imageFolder, str(i+1)))
            print("image fetch from url")
    return images
