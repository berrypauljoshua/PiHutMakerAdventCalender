from machine import Pin, PWM
import time

buzzer = PWM(Pin(22))

C = 523
D = 587
E = 659
G = 784

volume = 300

def play_tone(note, vol, delay_0, delay_1):
    buzzer.duty_u16(vol)
    buzzer.freq(note)
    time.sleep(delay_0)
    buzzer.duty_u16(0)
    time.sleep(delay_1)
    
play_tone(E, volume, 0.1, 0.2)
play_tone(E, volume, 0.1, 0.2)
play_tone(E, volume, 0.1, 0.5)

play_tone(E, volume, 0.1, 0.2)
play_tone(E, volume, 0.1, 0.2)
play_tone(E, volume, 0.1, 0.5)

play_tone(E, volume, 0.1, 0.2)
play_tone(G, volume, 0.1, 0.2)
play_tone(C, volume, 0.1, 0.2)
play_tone(D, volume, 0.1, 0.2)
play_tone(E, volume, 0.1, 0.2)