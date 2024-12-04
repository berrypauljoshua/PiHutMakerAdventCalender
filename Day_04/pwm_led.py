from machine import Pin, ADC, PWM
import time

pot = ADC(Pin(26))

red_led = PWM(Pin(18))
red_led.freq(100)
print(f"Red LED PWM Frequency = {red_led.freq()}")

while True:
    pot_val = pot.read_u16()
    print(f"Potentiometer Value = {pot_val}")
    
    red_led.duty_u16(pot_val)
    
    time.sleep(0.1)