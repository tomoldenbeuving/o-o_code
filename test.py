from microbit import *
import time

def sensorteller(afslag,sensor):
    while True:   
        sensor = display.read_light_level()
        t_end = time.time()
        seconds = 10
        afslag = 0 
        while time.time() < t_end + seconds:
            time.sleep(.1)
            if sensor < 120:
                afslag += 1
            if time.time == t_end: 
                break
