from os import listdir
from os.path import isfile, join
import cv2

PATH = "../assets"

def main():
    imgs = loadImages()
    untilIndex = len(imgs) - 1
    i = 0
    while True:
        cv2.imshow('image', imgs[i])
        
        if(i < untilIndex):
            i+=1
        else:
            i = 0
        
        if cv2.waitKey(1000) == ord('q'):
            break
        
    

def loadImages():
    return [cv2.imread(join(PATH,f)) for f in listdir(PATH) if isfile(join(PATH,f))]


if __name__ == '__main__':
    main()
    