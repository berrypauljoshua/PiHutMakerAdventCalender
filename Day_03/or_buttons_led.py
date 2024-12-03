from machine import Pin
import time

p_switch0 = Pin(10, Pin.IN, Pin.PULL_DOWN)
p_switch1 = Pin(11, Pin.IN, Pin.PULL_DOWN)
p_switch2 = Pin(12, Pin.IN, Pin.PULL_DOWN)

red_led = Pin(18, Pin.OUT)
amber_led = Pin(19, Pin.OUT)
green_led = Pin(20, Pin.OUT)

while True:
    time.sleep(0.2)
    
    if p_switch0.value() == 1 or p_switch1.value() == 1:
        green_led.value(1)
        time.sleep(2)
        green_led.value(0)
        print("p_switch0 or p_switch1 HIGH, Green LED blinking")