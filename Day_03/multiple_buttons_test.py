from machine import Pin
import time

p_switch0 = Pin(10, Pin.IN, Pin.PULL_DOWN)
p_switch1 = Pin(11, Pin.IN, Pin.PULL_DOWN)
p_switch2 = Pin(12, Pin.IN, Pin.PULL_DOWN)

while True:
    time.sleep(0.2)
    
    if p_switch0.value() == 1:
        print("p_switch0 HIGH")
    
    if p_switch1.value() == 1:
        print("p_switch1 HIGH")
        
    if p_switch2.value() == 1:
        print("p_switch2 HIGH")