from Line_Follower import *
#from Stepper import *

import RPi.GPIO as IO
IO.setmode(IO.BCM)

import signal

###############################

IO.setup(IR_Left, IO.IN) 
IO.setup(IR_Center, IO.IN) 
IO.setup(IR_Right,IO.IN)

IO.setup(en_l,IO.OUT)
IO.setup(en_r,IO.OUT)
IO.setup(M_Left1,IO.OUT)
IO.setup(M_Left2,IO.OUT)
IO.setup(M_Right1,IO.OUT)
IO.setup(M_Right2,IO.OUT)

IO.setup(switch,IO.OUT)

#IO.setup(T_EN,GPIO.OUT) # set enable pin as output
#IO.setup(M_EN,GPIO.OUT) # set enable pin as output
#IO.setup(B_EN,GPIO.OUT) # set enable pin as output

###############################

def keyboardInterruptHandler(signal, frame):
    print("KeyboardInterrupt (ID: {}) has been caught. Cleaning up...".format(signal))
    FDB_set("APP_Status", "OFF")
    FDB_set("RPi_Status", "OFF")
    FDB_set("Power", "OFF")
    IO.cleanup()
    print("Exiting the program")
    exit(0)
signal.signal(signal.SIGINT, keyboardInterruptHandler)

FDB_set("Power", "ON")


while True :
    
    STATUS = status()
    
    while STATUS == "\"ON\"" or STATUS == "ON":
        
        control(90)
        #FDB_set("Fruits", 1) #code for uploading fruit count
        STATUS = status()
    #stop()
        
while False :
    forward(100)
