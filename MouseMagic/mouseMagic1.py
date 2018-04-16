# -*- coding:UTF-8 -*-
import pyautogui as pag
import Tkinter as tk
from PIL import Image
import random
import time
import argparse
parser =argparse.ArgumentParser()
parser.add_argument('-r','--resultfile')
args=parser.parse_args()

resultfile=args.resultfile

root=tk.Tk()
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
window=Image.new("RGB",(screen_width,screen_height),(0,0,0))
print screen_height,screen_width
r=int(random.uniform(0,255))
g=int(random.uniform(0,255))
b=int(random.uniform(0,255))
print r,g,b
try:
    while True:
            r+=1
            g+=1
            b+=1
            if r==255:
                r=0
            if g==255:
                g=0
            if b==255:
                b=0
            time.sleep(0.01)
            x,y = pag.position() #返回鼠标的坐标
            if window.getpixel((x,y))[0]==0:
                window.putpixel((x,y),(r,g,b))
except  KeyboardInterrupt:
    window.resize((500,800))
    window.save(resultfile,'PNG')
    print 'save successfully....'
