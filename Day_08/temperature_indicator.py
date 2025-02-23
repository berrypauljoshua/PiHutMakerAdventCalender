from machine import Pin
import time, onewire, ds18x20

red_led = Pin(18, Pin.OUT)
amber_led = Pin(19, Pin.OUT)
blue_led = Pin(20, Pin.OUT)

sensor = ds18x20.DS18X20(onewire.OneWire(Pin(26, Pin.IN)))
sensors = sensor.scan()

while True:
    time.sleep(2)

    for id in sensors:
        sensor.convert_temp()

        time.sleep(5)

        temp_val = sensor.read_temp(id)

        print(temp_val, "°C")

        if temp_val <= 20:
            red_led.value(0)
            amber_led.value(0)
            blue_led.value(1)
        elif 20 < temp_val <= 24:
            red_led.value(0)
            amber_led.value(1)
            blue_led.value(0)
        elif temp_val > 24:
            red_led.value(1)
            amber_led.value(0)
            blue_led.value(0)
