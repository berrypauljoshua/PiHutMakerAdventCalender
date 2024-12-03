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
    
    if p_switch0.value() == 1 and p_switch1.value() == 1:
        red_led.value(0)
        amber_led.value(0)
        green_led.value(1)
        print("p_switch0 and p_switch1 HIGH, Green LED illuminated")
    elif p_switch1.value() == 1:
        print("p_switch1 HIGH, Amber LED illuminated")
        red_led.value(0)
        amber_led.value(1)
        green_led.value(0)
    else:
        print("p_switch0, p_switch1 and p_switch2 LOW, Red LED illuminated")
        red_led.value(1)
        amber_led.value(0)
        green_led.value(0)