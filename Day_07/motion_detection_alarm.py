from machine import Pin, PWM
import time

pir = Pin(21, Pin.IN, Pin.PULL_DOWN)

buzzer = PWM(Pin(22))

red_led = Pin(18, Pin.OUT)

print("PIR Warm Up...")
time.sleep(10)
print("PIR Warm Up Complete.")

def alarm():
    buzzer.duty_u16(300)
    
    for i in range(5):
        buzzer.freq(600)
        red_led.value(1)
        
        time.sleep(0.5)
        
        buzzer.freq(300)
        red_led.value(0)
        
        time.sleep(0.5)
        
    buzzer.duty_u16(0)
        
while True:
    if pir.value() == 1:
        alarm()
        
    time.sleep(0.01)