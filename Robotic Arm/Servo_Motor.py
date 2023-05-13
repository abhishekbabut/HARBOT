from gpiozero import AngularServo
from time import sleep

#servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)
servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)


def close():
    servo.angle = 90
    print("90")
    sleep(2)
    
    servo.angle = 90
    print("0")
    sleep(2)

def open1():
    servo.angle = -90
    print("-90")
    sleep(2)
    
    servo.angle = -90
    print("-90")
    sleep(2)
    


