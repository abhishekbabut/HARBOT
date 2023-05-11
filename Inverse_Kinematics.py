from numpy import *
from Stepper import TOP,MID,BOTTOM
from Servo_Motor import *

a1 = 24  # length of link a2 in cm
a2 = 16  # length of link a4 in  cm

# Desired Position of End effector
#x = 5
#y = 3

def inverse(x,d):
    d1=sqrt((0-a1)**2+(0-a2)**2)
    d2=sqrt((0-x)**2+(0-d)**2)
    
    
    if(d<40):
    # Equations for Inverse kinematics
        r = sqrt(x**2+d**2)  # eqn 1
        alpha = arccos((a2**2+a1**2-r**2)/(2*a1*a2))  # eqn 2
        
        theta_2=pi-alpha
        
        a2_sin_theta_2=sqrt(1-cos(theta_2**2))
        a2_cos_theta_2=a2*cos(theta_2)
        side_length=a1+a2_cos_theta_2
        beta=arctan2(a2_sin_theta_2,side_length)
        
        
        theta_1 = (arctan2(d,x))-beta
        
        
        theta_2 = rad2deg(theta_2)
        theta_1=rad2deg(theta_1)
        print(theta_1)
        s1=int(8.88*theta_1)
        s2=int(8.88*theta_2)
        print(s1)
        print(s2)
        MID('ant',s2)
        tb=BOTTOM('ant',s1)
        print(tb)
        if tb==1:
            MID('clk',s2)
            BOTTOM('clk',s1)
            open1()
    else:
        print("un reachable")