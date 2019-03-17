from os import listdir
from os.path import isfile, join
import cv2
import time

PATH = "../assets"
FADE_TIME = 0.07
CV2_SHOW_NAME = 'image'

def main():
    imgs = loadImages()
    untilIndex = len(imgs) - 1
    i = 0
    while True:
        cv2.imshow(CV2_SHOW_NAME, imgs[i])
        
        before = i
        if(i < untilIndex):
            i+=1
        else:
            i = 0
        
        if cv2.waitKey(1000) == ord('q'):
            break
        
        transitionFade(imgs[before],imgs[i])

def transitionFade(fadeOut, fadeIn):
    for x in range(10):
        fade = x/10.0
        dst = cv2.addWeighted(fadeOut, 1-fade, fadeIn, fade, 0)
        cv2.imshow(CV2_SHOW_NAME, dst)
        cv2.waitKey(1)
        time.sleep(FADE_TIME)

    

def loadImages():
    return [cv2.imread(join(PATH,f)) for f in listdir(PATH) if isfile(join(PATH,f))]


if __name__ == '__main__':
    main()
    
