#code for auto ssa reroll in bss :sob: i dont even know why i needed this


import cv2
from matplotlib import text
import mouse
import pytesseract
import numpy as np
from PIL import ImageGrab
import keyboard as keyb
import threading
import time
"""+x2.5 Capac
+57% Blue Pollen
++51% Red Pollen
+69% White Pollen
++18% Pollen

+4% Bee Ability Rate
+Passive: Pop Star

"""
run = False
def click():
    keyb.press_and_release("e")
    time.sleep(2)
    mouse.click("left")


def check(text):
    yes = 0
    text = text.splitlines()
    temp = []
    flag = False
    for res in text:
        res = res.lower()
        if "red" in res or "white" in res or "beegather" in res or "instant" in res or "capacity" in res:
            
            continue
        if "pop" in res:
            flag = True
        temp.append(res)
    if not flag:
        return False
    print(temp, "temp")
    for line in temp:
        if "blue" in line:
            yes+=1
        elif "ability" in line:
            yes+=1
        elif "pollen" in line:
            yes+=1
        elif "convert" in line:
            yes+=1
        elif "critical" in line:
            yes+=1

        if yes >= 5 and flag:
            return True

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)
def re():
    # Define the coordinates (left, top, right, bottom)
    bbox = (1002, 475, 1170, 588)

    # Grab screenshot region (PIL Image, already in memory)
    pil_img = ImageGrab.grab(bbox=bbox)

    # Convert PIL image → NumPy array
    img = np.array(pil_img)
    
    # PIL uses RGB, OpenCV uses BGR
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    _, thresh = cv2.threshold(
        gray, 120, 255, cv2.THRESH_BINARY
    )
    # Preprocess
    config = "--psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"
    text = pytesseract.image_to_string(thresh, config=config)
    # OCR
    print(text)
    return check(text)

keyb.add_hotkey("x" , re)

def yes():
    while True:
        click()
        time.sleep(1)
        f = re()
        if f:
            print("found")
            run = False
            break

        time.sleep(1)


def start():
    global run
    run = (True if run == False else False)
    if run:
        print("start")
        threading.Thread(target=yes).start()

keyb.add_hotkey("x" , start)

keyb.wait('esc')