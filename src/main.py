from os import listdir
from os.path import isfile, join
import cv2
import time
import numpy as np

PATH = join('..', 'assets')
FADE_TIME = 0.07
CV2_SHOW_NAME = 'image'

def main():
    imgs = loadImages()
    imgs = applyBorder(imgs)
    waterMark = cv2.imread(join('..', 'linkedin.jpg'))
    waterMark = cv2.resize(waterMark, (50, 50))
    untilIndex = len(imgs) - 1
    i = -1
    while True:
        
        before = i
        if(i < untilIndex):
            i+=1
        else:
            i = 0
        
        transitionFade(imgs[before],imgs[i], waterMark)
        
        if cv2.waitKey(2000) == ord('q'):
            break
        

def transitionFade(fadeOut, fadeIn, waterMark):
    for x in range(10):
        fade = x/10.0
        dst = cv2.addWeighted(fadeOut, 1-fade, fadeIn, fade, 0)
        #print(dst[120:170,20:70].shape)
        dst[120:170,20:70] = cv2.addWeighted(dst[120:170,20:70], .7, waterMark, .3, 0)
        cv2.imshow(CV2_SHOW_NAME, dst)
        if cv2.waitKey(100) == ord('q'):
            exit(0)

def applyBorder(imgs):
    return [cv2.copyMakeBorder(img,20,20,20,20,cv2.BORDER_CONSTANT,value=(0, 0, 255)) for img in imgs]
    

def loadImages():
    return [cv2.imread(join(PATH,f)) for f in listdir(PATH) if isfile(join(PATH,f))]


if __name__ == '__main__':
    main()
    
