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
    
    if p_switch0.value() == 1:
        red_led.toggle()
        print("p_switch0 HIGH, toggling Red LED")
    elif p_switch1.value() == 1:
        amber_led.toggle()
        print("p_switch1 HIGH, toggling Amber LED")
    elif p_switch2.value() == 1:
        green_led.toggle()
        print("p_switch2 HIGH, toggling Green LED")