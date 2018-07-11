import RPi.GPIO as GPIO

idSensorAgua=40
idSensorComida=38
idSensorLuz=40

def iniciar_sensores():
    print("iniciando sensores")
    # GPIO.setmode(GPIO.BCM)

def hay_agua():
    return "SI"

def hay_comida():
    return "NO"

def estado_luz():
    if(GPIO.input(idSensorLuz)):
        return "SI"
    else:
        return "NO"


def finalizar_sensores():
    print("finalizar sensores")


