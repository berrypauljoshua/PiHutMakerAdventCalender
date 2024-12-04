from machine import Pin, ADC
import time

pot = ADC(Pin(26))

red_led = Pin(18, Pin.OUT)

while True:
    pot_val = pot.read_u16()
    t_delay = pot_val / 65535
    print(f"Potentiometer Value = {pot_val}, Time Delay = {t_delay}")
    
    red_led.value(1)
    time.sleep(t_delay)

    red_led.value(0)
    time.sleep(t_delay)