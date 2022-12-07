import requests
from PIL import Image

defaultWidthHeight = "640/360"


def parseWidthHeight(widthHeight):
    if widthHeight:
        tmp = widthHeight.split("/")
        width = int(tmp[0])
        height = int(tmp[1])
        return width, height
    else:
        return 640, 360


def validWidthHeight(widthHeight):
    tmp = widthHeight.split("/")
    try:
        width = int(tmp[0])
        height = int(tmp[1])
        if width <= 0 or height <= 0:
            return False
        return True
    except Exception as e:
        return False



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


def fetchImage(imageFolder, i, fetchWidthHeight):
    if fetchWidthHeight:
        if not validWidthHeight(fetchWidthHeight):
            print("Invalid format of width/height!")
            exit()
        fetchFromURL(fetchWidthHeight, imageFolder, str(i+1))
        print("image", i+1, end = " ")
        print("fetch from url")
    else:
        print("image", i+1, end = " ")
        try:
            open(f"{imageFolder}/{i+1}.png")
            print("fetch from local")
        except:
            fetchFromURL(defaultWidthHeight, imageFolder, str(i+1))
            print("fetch from url")


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
