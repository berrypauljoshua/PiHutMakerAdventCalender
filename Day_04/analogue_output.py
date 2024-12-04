from machine import Pin, ADC
import time

pot = ADC(Pin(26))

while True:
    print(pot.read_u16())
    time.sleep(0.1)