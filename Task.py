import numpy as np
import time
import cv2
from mss import mss
import os
from screeninfo import get_monitors
from PIL import Image
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController



def getPos(img):
    img_rgb = Image.frombytes('RGB', (width, height), sct.grab(monitor).rgb)
    pic1 = cv2.cvtColor(np.array(img_rgb), cv2.COLOR_RGB2GRAY)

    result = cv2.matchTemplate(img, pic1, method)
    mn, _, mnLoc, _ = cv2.minMaxLoc(result)
    MPx, MPy = mnLoc
    trows, tcols = img.shape[:2]
    x = int(MPx + tcols / 2)
    y = int(MPy + trows / 2)
    return x, y


x = os.path.dirname(os.path.abspath(__file__))
sct = mss()
width = 0
height = 0
m = 0

for monitor in get_monitors():
    width += monitor.width
    height = monitor.height
    m += 1
w = int(width*(m-1)/m)
monitor = {'top': 0, 'left': int(-width*(m-1)/m),
           'width': width, 'height': height}

method = cv2.TM_SQDIFF_NORMED

# 138922875

card = cv2.imread(x+'.\\card.png')
card = cv2.cvtColor(np.array(card), cv2.COLOR_BGR2GRAY)

mainpage = cv2.imread(x+'.\\mainpage.png')
mainpage = cv2.cvtColor(np.array(mainpage), cv2.COLOR_BGR2GRAY)

super7 = cv2.imread(x+'.\\super7.png')
super7 = cv2.cvtColor(np.array(super7), cv2.COLOR_BGR2GRAY)

window = cv2.imread(x+'.\\window.png')
window = cv2.cvtColor(np.array(window), cv2.COLOR_BGR2GRAY)

confirm = cv2.imread(x+'.\\confirm.png')
confirm = cv2.cvtColor(np.array(confirm), cv2.COLOR_BGR2GRAY)

search = cv2.imread(x+'.\\search.png')
search = cv2.cvtColor(np.array(search), cv2.COLOR_BGR2GRAY)

t1 = time.time()

keyboard = KeyboardController()


def typetext(text):
    for i in range(len(text)):
        keyboard.press(f"{text[i]}")
        keyboard.release(f"{text[i]}")
        time.sleep(0.05)


# to window
x, y = getPos(window)
mouse = MouseController()
mouse.position = (x - w, y)
time.sleep(0.05)
mouse.click(Button.left)
time.sleep(0.5)
# for i in range(loops):
num = 0
while True:

    for i in range(27):
        keyboard.press(Key.right)
        keyboard.release(Key.right)
        time.sleep(0.5)

    x, y = getPos(super7)
    mouse = MouseController()
    mouse.position = (x - w, y)
    time.sleep(0.5)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)

    x, y = getPos(card)
    mouse = MouseController()
    mouse.position = (x - w, y)
    time.sleep(0.5)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)

    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
    time.sleep(20)

    x, y = getPos(search)
    mouse = MouseController()
    mouse.position = (x - w, y)
    time.sleep(0.05)
    x, y = getPos(confirm)
    mouse = MouseController()
    mouse.position = (x - w, y)
    time.sleep(0.5)

    keyboard.press("w")
    keyboard.release("w")
    time.sleep(1)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)

    typetext("138922875")
    time.sleep(1)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)

    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(2)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)

    keyboard.press(Key.space)
    time.sleep(85)
    keyboard.release(Key.space)

    time.sleep(0.5)

    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    time.sleep(3)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(30)

    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    time.sleep(0.5)

     

    num += 1
    print(f"已執行 {num} 次", end='\r')

 