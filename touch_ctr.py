import pyautogui
from time import sleep
from touch_utility import read_touch_coordinates

surfaceX=480
surfaceY=320

ratioX=surfaceX / 255
ratioY=surfaceY / 230

prevX = 0
prevY=0
while True:
  touch_x, touch_y = read_touch_coordinates()
  if touch_x != 255 and touch_y !=0:
    pyautogui.moveTo(round(touch_x * ratioX),round(touch_y * ratioY),duration=0.25)
  if touch_x == prevX and touch_y == prevY and touch_x != 255 and touch_y != 0:
    pyautogui.click()
  prevX = touch_x
  prevY=touch_y
  sleep(0.1)
  
  
