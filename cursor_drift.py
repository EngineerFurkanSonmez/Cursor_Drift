import time
import pyautogui

try:
    while True:
        x, y = pyautogui.position()
        pyautogui.moveTo(x + 1, y)
        pyautogui.moveTo(x - 1, y)
        time.sleep(30)
except KeyboardInterrupt:
    print("Script stopped.")
