import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import time
from Servo_Motor import *
GPIO.setmode(GPIO.BCM)

T_STEP = 2 # Step GPIO Pin
T_DIR = 3 # Direction (DIR) GPIO Pin
T_EN = 4 # enable pin (LOW to enable)

M_STEP = 10 # Step GPIO Pin
M_DIR = 9 # Direction (DIR) GPIO Pin
M_EN = 11 # enable pin (LOW to enable)

B_STEP = 25 # Step GPIO Pin
B_DIR = 8 # Direction (DIR) GPIO Pin
B_EN = 7 # enable pin (LOW to enable)

# Declare a instance of class pass GPIO pins numbers and the motor type
Top = RpiMotorLib.A4988Nema(T_DIR, T_STEP, (21,21,21), "DRV8825")
GPIO.setup(T_EN,GPIO.OUT) # set enable pin as output

# Declare a instance of class pass GPIO pins numbers and the motor type
Mid = RpiMotorLib.A4988Nema(M_DIR, M_STEP, (21,21,21), "DRV8825")
GPIO.setup(M_EN,GPIO.OUT) # set enable pin as output

# Declare a instance of class pass GPIO pins numbers and the motor type
Bot = RpiMotorLib.A4988Nema(B_DIR, B_STEP, (21,21,21), "DRV8825")
GPIO.setup(B_EN,GPIO.OUT) # set enable pin as output

###########################
# Actual motor control
###########################
#
def TOP(dir,s3): 
    if (dir == "ant"):
        GPIO.output(T_EN,GPIO.LOW) # pull enable to low to enable motor
        Top.motor_go(False, # True=Clockwise, False=Counter-Clockwise
                             "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                             s3, # number of steps
                             .0005, # step delay [sec]
                             False, # True = print verbose output 
                             .05) # initial delay [sec]
        print('ATOP')
        #time.sleep(5)
    if (dir == "clk"):
        GPIO.output(T_EN,GPIO.LOW) # pull enable to low to enable motor
        Top.motor_go(True, # True=Clockwise, False=Counter-Clockwise
                             "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                             s3, # number of steps
                             .0005, # step delay [sec]
                             False, # True = print verbose output 
                             .05) # initial delay [sec]
        
        print("Top")
        
def MID(dir,s2): 
    if (dir == "ant"):
        GPIO.output(M_EN,GPIO.LOW) # pull enable to low to enable motor
        Mid.motor_go(False, # True=Clockwise, False=Counter-Clockwise
                             "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                             s2, # number of steps
                             .0005, # step delay [sec]
                             False, # True = print verbose output 
                             .05) # initial delay [sec]
        print('AMid')
    if (dir == "clk"):
        GPIO.output(M_EN,GPIO.LOW) # pull enable to low to enable motor
        Mid.motor_go(True, # True=Clockwise, False=Counter-Clockwise
                             "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                             s2, # number of steps
                             .0005, # step delay [sec]
                             False, # True = print verbose output 
                             .05) # initial delay [sec]
        
        print("MID")
def BOTTOM(dir,s1): 
    if (dir == "ant"):
        GPIO.output(B_EN,GPIO.LOW) # pull enable to low to enable motor
        Bot.motor_go(False, # True=Clockwise, False=Counter-Clockwise
                             "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                             s1, # number of steps
                             .0005, # step delay [sec]
                             False, # True = print verbose output 
                             .05) # initial delay [sec]
        print('ABOT')
        close()
        return 1
    
    if (dir == "clk"):
        
        GPIO.output(B_EN,GPIO.LOW) # pull enable to low to enable motor
        Bot.motor_go(True, # True=Clockwise, False=Counter-Clockwise
                             "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                             s1, # number of steps
                             .0005, # step delay [sec]
                             False, # True = print verbose output 
                             .05) # initial delay [sec]
        
        print("Bot")
        #open1()
#while True:
#TOP("ant",600)
#MID("clk",600)
#BOTTOM("clk",600)

#GPIO.cleanup() # clear GPIO allocations after run