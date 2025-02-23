from machine import Pin, PWM
import time, onewire, ds18x20

red_led = Pin(18, Pin.OUT)
amber_led = Pin(19, Pin.OUT)
blue_led = Pin(20, Pin.OUT)

buzzer = PWM(Pin(22))
buzzer.duty_u16(0)

sensor = ds18x20.DS18X20(onewire.OneWire(Pin(26, Pin.IN)))
sensors = sensor.scan()

def alarm():
    buzzer.duty_u16(300)
    
    for i in range(5):
        buzzer.freq(600)
        
        blue_led.value(1)

        time.sleep(0.2)

        blue_led.value(0)

        time.sleep(0.2)

    buzzer.duty_u16(0)

while True:
    time.sleep(2)

    for id in sensors:
        sensor.convert_temp()
    
        time.sleep(5)

        temp_val = sensor.read_temp(id)

        print(temp_val, "°C")

        if temp_val < 20:
            alarm() 
