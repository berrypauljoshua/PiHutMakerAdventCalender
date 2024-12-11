from machine import Pin
import time

pir = Pin(21, Pin.IN, Pin.PULL_DOWN)

green_led = Pin(20, Pin.OUT)

print("PIR Warm Up...")
time.sleep(10)
print("PIR Warm Up Complete.")

while True:
    if pir.value() == 1:
        green_led.value(1)
        print("Motion Detected!")
    else:
        green_led.value(0)
        
    time.sleep(0.01)
