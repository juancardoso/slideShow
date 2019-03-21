from os import listdir
from os.path import isfile, join
import cv2
import time
import numpy as np

PATH = "../assets"
FADE_TIME = 0.07
CV2_SHOW_NAME = 'image'

def main():
    imgs = loadImages()
    imgs = applyBorder(imgs)
    waterMark = cv2.imread('../spacex.png', cv2.IMREAD_UNCHANGED)
    waterMark = cv2.resize(waterMark, (50, 50))
    print(waterMark.shape)
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
    imgs = [cv2.imread(join(PATH,f), cv2.IMREAD_UNCHANGED) for f in listdir(PATH) if isfile(join(PATH,f))]
    for i in range(len(imgs)):
        img = imgs[i]
        b_channel, g_channel, r_channel = cv2.split(img)
        alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 50 
        imgs[i] = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))
    return imgs


if __name__ == '__main__':
    main()
    
