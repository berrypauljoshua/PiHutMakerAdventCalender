from machine import Pin,
import time, onewire, ds18x20

sensor = ds18x20.DS18X20(onewire.OneWire(Pin(26,Pin.IN)))
sensors = sensor.scan()

while True:
    sensor.convert_temp()

    time.sleep(2)

    for id in sensors:
        print((sensor.read_temp(id)), "°C")

        time.sleep(5)
