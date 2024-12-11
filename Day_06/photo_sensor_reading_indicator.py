from machine import Pin, ADC, PWM
import time

photo_sensor = ADC(Pin(27))

red_led = Pin(18, Pin.OUT)
amber_led = Pin(19, Pin.OUT)
green_led = Pin(20, Pin.OUT)

buzzer = PWM(Pin(22))
buzzer.freq(300)

while True:
    photo_val = round((photo_sensor.read_u16() / 65535) * 100)
    
    print(f"Phototransistor Value = {photo_val}%")

    if photo_val <= 30:
        red_led.value(0)
        amber_led.value(0)
        green_led.value(1)
        
        buzzer.duty_u16(0)
        
        print("Light Level Low, Green LED Illuminated")
    elif 30 < photo_val <= 60:
        red_led.value(0)
        amber_led.value(1)
        green_led.value(1)
        
        buzzer.duty_u16(0)
        
        print("Light Level Medium, Green and Amber LED Illuminated")
    elif 60 < photo_val <= 100:
        red_led.value(1)
        amber_led.value(1)
        green_led.value(1)
        
        buzzer.duty_u16(300)
        
        print("Light Level High, Green, Amber and Red LED Illuminated")
 
    time.sleep(0.1)