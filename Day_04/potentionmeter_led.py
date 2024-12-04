from machine import Pin, ADC
import time

pot = ADC(Pin(26))

red_led = Pin(18, Pin.OUT)
amber_led = Pin(19, Pin.OUT)
green_led = Pin(20, Pin.OUT)

while True:
    pot_val = pot.read_u16()
    print(f"Potentiometer Value = {pot_val}")
    
    if pot_val <= 20000:
        red_led.value(1)
        amber_led.value(0)
        green_led.value(0)
    elif 20000 < pot_val < 40000:
        red_led.value(0)
        amber_led.value(1)
        green_led.value(0)
    elif pot_val >= 40000:
        red_led.value(0)
        amber_led.value(0)
        green_led.value(1)
    
    time.sleep(0.1)