from ut import *
from Stepper_Motors import *
from Red_Circle_Detection import *

def harvest():
    a=0
    while a<=4800:
        red=color()
        if red==0:
            TOP('clk',800)
        if red==1:
            getObjects()
            time.sleep(2)
        a=a+800
        
    if a>4800:
        TOP('ant',4800)
   
