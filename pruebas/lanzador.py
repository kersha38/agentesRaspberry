import threading
from pruebas.actuador import *
import RPi.GPIO as GPIO
import time

def empezar_hilos(arr_hilos):
    for hilo in arr_hilos:
        hilo.start()

def actuar(actuador):
    try:
        while True:
            actuador.abrir_agua()
            time.sleep(2)
    finally:
        actuador.finalizar_actuadores()


GPIO.setmode(GPIO.BOARD)
hilos = []
actuador = Actuador()
hilo_actuar = threading.Thread(target=actuar, args=(actuador))
hilos.append(hilo_actuar)
empezar_hilos(hilos)