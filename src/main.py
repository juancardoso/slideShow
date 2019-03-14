from os import listdir
from os.path import isfile, join
import cv2

PATH = "../assets"

def main():
    imgs = loadImages()
    
    

def loadImages():
    return [cv2.imread(join(PATH,f)) for f in listdir(PATH) if isfile(join(PATH,f))]


if __name__ == '__main__':
    main()
    