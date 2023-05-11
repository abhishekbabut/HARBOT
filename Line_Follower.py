import RPi.GPIO as IO
import time
import pyrebase
from config import *
from UT_main import *

IO.setwarnings(False)
IO.setmode(IO.BCM)

#IR_setup
IR_Left = 17
IR_Center = 15
IR_Right = 27
IO.setup(IR_Left, IO.IN) 
IO.setup(IR_Center, IO.IN) 
IO.setup(IR_Right,IO.IN) 

global IR_out
global prev_Status
prev_Status = "null"

global sharp_turn
sharp_turn = "null"

#motor_setup

en_l = 12
M_Left1 = 16
M_Left2 = 20
en_r = 13
M_Right1 = 19
M_Right2 = 26
IO.setup(en_l,IO.OUT)
IO.setup(en_r,IO.OUT)
IO.setup(M_Left1,IO.OUT)
IO.setup(M_Left2,IO.OUT)
IO.setup(M_Right1,IO.OUT)
IO.setup(M_Right2,IO.OUT) 

l = IO.PWM(en_l,1000)		#create PWM instance with frequency
r = IO.PWM(en_r,1000)		#create PWM instance with frequency

#FIREBASE
config = config()
firebase = pyrebase.initialize_app(config)
user = "user1"
storageBucket = "HARBOT/" + user

#Remote_switch
switch = 21
IO.setup(switch,IO.OUT)

def forward(dutycycle):
    l.start(dutycycle)				#start PWM of required Duty Cycle 
    r.start(dutycycle)				#start PWM of required Duty Cycle 
    IO.output(M_Left2,True)
    IO.output(M_Left1,False)
    IO.output(M_Right2,False)
    IO.output(M_Right1,True) 
    print("FORWARD")


def left(dutycycle):
    l.start(dutycycle)				#start PWM of required Duty Cycle 
    r.start(dutycycle)				#start PWM of required Duty Cycle
    #l.start(80)				#start PWM of required Duty Cycle 
    IO.output(M_Left1,True) 
    IO.output(M_Left2,False) #False
    IO.output(M_Right1,True) #TRUE 
    IO.output(M_Right2,False)
    print("Left Turn")
    harvest()

def right(dutycycle):
    l.start(dutycycle)				#start PWM of required Duty Cycle 
    r.start(dutycycle)				#start PWM of required Duty Cycle 
    IO.output(M_Left1,False) 
    IO.output(M_Left2,True) # Forward
    IO.output(M_Right1,False) 
    IO.output(M_Right2,True) #Reverse
    print("Right Turn")
    
def stop(dutycycle):
    IO.output(en_l,False)				#start PWM of required Duty Cycle 
    IO.output(en_r,False)
    IO.output(M_Left1,True) 
    IO.output(M_Right1,True)
    IO.output(M_Left2,True) 
    IO.output(M_Right2,True)
    harvest()
    
def IRread():
    global IR_out
    IR_out = str(IO.input(IR_Left)) + str(IO.input(IR_Center)) + str(IO.input(IR_Right))
    #01 : Frontleft 10: Right front
    print(IR_out)
    # return IR_out



def status():
    
    database = firebase.database()
    ProjectBucket = database.child(storageBucket)                            
    Status = ProjectBucket.child("APP_Status").get().val()
    #print(Status)
    global prev_Status
    
    if prev_Status != Status:
        
        if str(Status) == "OFF" or str(Status) == "\"OFF\"" :
            IO.output(en_l,False)				#start PWM of required Duty Cycle 
            IO.output(en_r,False)
            FDB_set("RPi_Status", "OFF")
            print("HARBOT is now OFF.")
            IO.output(switch, IO.LOW)
        else:
            FDB_set("RPi_Status", "ON")
            print("HARBOT now is ON.")
            IO.output(switch, IO.HIGH)
        
    #global prev_Status
    prev_Status = Status
    return Status

def FDB_set(key, value):
    
    database = firebase.database()
    ProjectBucket = database.child(storageBucket)                            
    Status = ProjectBucket.child(key).set(value)
    
    
def control(speed):
    
    IRread()
    global sharp_turn
    
    #FORWARD
    if IR_out == "010":
        forward(speed)

    #TURN RIGHT
    elif IR_out == "001": 
        right(speed)
        sharp_turn = "right"
    elif IR_out == "011": 
        right(speed)   
    
    #TURN LEFT
    elif IR_out == "100": 
        left(speed)
    elif IR_out == "110" :
        left(speed)
        sharp_turn = "left"
         
    elif IR_out == "000":
       if sharp_turn == "right":
          right(speed)
       if sharp_turn == "left":
          left(speed)
       else:
          stop(100)
          
    else:
        stop(100)
     
# while True:
#     status()
#     while Status == "\"ON\"":
#         IRread()
#         control(100)
#         status()
    
#         status()  

#!these blocks are not executed   
IO.cleanup() #resets defined pins as input
