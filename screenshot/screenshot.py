import time
import pyautogui
time.sleep(5)
img = pyautogui.screenshot()

img.save("screenshot.png")
