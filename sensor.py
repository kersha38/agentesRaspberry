import RPi.GPIO as GPIO
import time

idSensorAgua=31
idSensorComida=29
idSensorLuz=40

def iniciar_sensores():
    print("iniciando sensores")
    # GPIO.setmode(GPIO.BOARD)
    GPIO.setup(idSensorComida,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(idSensorAgua,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

def hay_agua():
    if(GPIO.inpu(idSensorAgua)):
        return "SI"
    else:
        return "NO"

def hay_comida():
    if(GPIO.input(idSensorComida)):
        return "SI"
    else:
        return "NO"

def estado_luz():
    if(GPIO.input(idSensorLuz)):
        return "SI"
    else:
        return "NO"


def finalizar_sensores():
    print("finalizar sensores")

def obtenerHora():
    return time.strftime("%H:%M:%S")

def obtenerFecha():
    return time.strftime("%d/%m/%y")
