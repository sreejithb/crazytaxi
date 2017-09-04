"""
All coordinates assume a screen resolution of 1920x1080, and Chrome
maximized with the Bookmarks Toolbar enabled.
Down key has been hit 4 times to center play area in browser.
x_pad = 156
y_pad = 345
Play area =  x_pad+1, y_pad+1, 796, 825
"""
import pyscreenshot as ImageGrab
import os
import time
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import numpy as np
import pytesseract
from PIL import Image

# Globals
# ------------------
x_pad = 1029
y_pad = 292

start_button_x = 161
start_button_y = 279
second_start_button_x = 309
second_start_button_y = 360

score_x1 = 96
score_y1 = 5
score_x2 = 204
score_y2 = 31

tessdata_dir_config = '--tessdata-dir "."'

def screenGrab():
    box = (x_pad+1, y_pad+1, x_pad+620, y_pad+413)
    im = ImageGrab.grab(box)
    im_np = np.array(im)
    im = ImageGrab.grab(box)
    im_np = im_np - np.array(im)
    print im_np
    im_fin = Image.fromarray(im_np)
    im_fin.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')

def start_game(m):
    m.click(x_pad + start_button_x, y_pad+start_button_y)
    m.click(x_pad + second_start_button_x, y_pad + second_start_button_y)



def start_game_play(k):
    all_keys = [k.up_key,k.down_key,k.left_key,k.right_key]
    while(True):
        #r = np.random.randint(low=0,high = len(all_keys))
        k.tap_key(k.space)
        #box = (x_pad + score_x1 + 1, y_pad + score_y1 + 1, x_pad + score_x2 + 1, y_pad + score_y2 + 1)
        #im = ImageGrab.grab(box)
        #print im
        #fname = 'full_snap_' + str(int(time.time())) + '.png'
        #print fname
        #im.save(fname,'PNG')
        #print fname
        #i = Image.open(fname)
        #text = pytesseract.image_to_string(Image.open(fname),config=tessdata_dir_config)
        #print text


def main():
    m = PyMouse()
    k = PyKeyboard()
    screenGrab()
    start_game(m)
    start_game_play(k)


if __name__ == '__main__':
    main()