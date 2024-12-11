from machine import Pin, ADC

photo_sensor = ADC(Pin(27))

photo_val = photo_sensor.read_u16()

print(photo_val)