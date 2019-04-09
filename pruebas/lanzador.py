from actuador import *
import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BOARD)
actuador = Actuador()
try:
    while True:
        actuador.abrir_agua()
        time.sleep(2)
finally:
    actuador.finalizar_actuadores()
