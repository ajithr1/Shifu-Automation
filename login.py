from uiautomator import device as d
from uiautomator import Device
from time import sleep
import os

d(text="thome").click()
sleep(5)
print("open t.home")
d(text="Smart Home").click()
sleep(5)
print("In Smart Home")
