import numpy as np
import time
import cv2
from mss import mss
import os
from screeninfo import get_monitors
from PIL import Image
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import pyautogui

def wait_for_image(image_path, timeout=1):
    start_time = time.time()
    
    while True:
        # Search for the image on the screen
        image_location = pyautogui.locateOnScreen(image_path, grayscale=True, confidence=0.65)
     
        if image_location is not None:
            # Image found
            x, y, _, _ = image_location
            #print(x, y)
            return x, y
        
        # Check if timeout has been reached
        if time.time() - start_time > timeout:
            # Timeout reached
            continue
        
        # Sleep for a short duration before searching again
        time.sleep(0.5)


def getPos(img):
    img_rgb = Image.frombytes('RGB', (width, height), sct.grab(monitor).rgb)
    pic1 = cv2.cvtColor(np.array(img_rgb), cv2.COLOR_RGB2GRAY)
    trows, tcols = img.shape[:2]

    result = cv2.matchTemplate(img, pic1, method)

                               
    mn, _, mnLoc, _ = cv2.minMaxLoc(result)
    MPx, MPy = mnLoc
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

regera = cv2.imread(x+'.\\regera.png')
regera = cv2.cvtColor(np.array(regera), cv2.COLOR_BGR2GRAY)

enter = cv2.imread(x+'.\\enter.png')
enter = cv2.cvtColor(np.array(enter), cv2.COLOR_BGR2GRAY)

esc = cv2.imread(x+'.\\esc.png')
esc = cv2.cvtColor(np.array(esc), cv2.COLOR_BGR2GRAY)

anna = cv2.imread(x+'.\\anna.png')
anna = cv2.cvtColor(np.array(anna), cv2.COLOR_BGR2GRAY)



keyboard = KeyboardController()


def typetext(text):
    for i in range(len(text)):
        keyboard.press(f"{text[i]}")
        keyboard.release(f"{text[i]}")
        time.sleep(0.05)


# to window
# x, y = getPos(window)
x, y = wait_for_image(window)
mouse = MouseController()
mouse.position = (x - w, y)
time.sleep(0.05)
mouse.click(Button.left)
time.sleep(0.5)
# for i in range(loops):
num = 0
while True:
    t1 = time.time()

    
    #for i in range(27):
    #    keyboard.press(Key.right)
    #   keyboard.release(Key.right)
    #   time.sleep(0.5)
    
    start_time = time.time()
    timeout = 0.3
    
    while True:
        # Search for the image on the screen
        image_location = pyautogui.locateOnScreen(super7, grayscale=True, confidence=0.5)
        
        if image_location is not None:
            # Image found
            px, y, _, _ = image_location
            break
        
        # Check if timeout has been reached
        if time.time() - start_time > timeout:
            # Timeout reached
            keyboard.press(Key.right)
            keyboard.release(Key.right)
            
        
        # Sleep for a short duration before searching again
        time.sleep(0.1)

    #x, y = getPos(super7)
    x, y = wait_for_image(super7)
    mouse = MouseController()
    mouse.position = (x - w, y)
    time.sleep(0.5)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)

    #x, y = getPos(card)
    x, y = wait_for_image(card)
    mouse = MouseController()
    mouse.position = (x - w, y)
    time.sleep(0.5)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)

    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
    time.sleep(1.5)
    x, y = wait_for_image(confirm)

    #x, y = getPos(search)
    x, y = wait_for_image(search)
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

	
    #x, y = wait_for_image(regera)
    keyboard.press(Key.space)
    x, y = wait_for_image(esc)
    keyboard.release(Key.space)

    time.sleep(0.5)

    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    time.sleep(2)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    # time.sleep(1)
    # #x, y = wait_for_image(anna)
    # time.sleep(25)

    x, y = wait_for_image(window)
    mouse = MouseController()
    mouse.position = (x - w, y - 50)
    time.sleep(0.05)
    mouse.click(Button.left)

    x, y = wait_for_image(mainpage)
    mouse.position = (x - w, y)
    time.sleep(0.05)
    mouse.click(Button.left)


     

    num += 1
    t2 = time.time()
    print(f"已執行 {num} 次 ({round(t2-t1, 2)}s)   ", end='\r')

 