from machine import Pin, ADC, PWM
import time

pot = ADC(Pin(26))
buzzer = PWM(Pin(22))
buzzer.freq(500)

while True:
    pot_val = pot.read_u16()
    print(f"Potentiometer Value = {pot_val}")
    
    buzzer.duty_u16(pot_val)