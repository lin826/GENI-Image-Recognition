from fetchImg import *

numOfImage = 5

images = []



if __name__ == '__main__':
    images = fetchImages(numOfImage)

    for i in range(numOfImage):
        images[i].show()

