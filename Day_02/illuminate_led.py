from machine import Pin
import time

red_led = Pin(18, Pin.OUT)
amber_led = Pin(19, Pin.OUT)
green_led = Pin(20, Pin.OUT)

red_led.value(1)
amber_led.value(1)
green_led.value(1)

time.sleep(5)

red_led.value(0)
amber_led.value(0)
green_led.value(0)