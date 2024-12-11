from machine import Pin, ADC

photo_sensor = ADC(Pin(27))

photo_val = photo_sensor.read_u16()

photo_val_percentage = round((photo_val / 65535) * 100)

print(f"{photo_val_percentage}%")