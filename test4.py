import pyautogui
import keyboard
import time

while 1:
    if pyautogui.pixel(609, 440)[0] == 235:
        keyboard.press('x')
        time.sleep(0.1)
        keyboard.release('x')
    if pyautogui.pixel(609, 440)[0] == 67:
        keyboard.press('z')
        time.sleep(0.1)
        keyboard.release('z')
    time.sleep(0.01)

