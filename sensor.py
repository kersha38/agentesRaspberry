import RPi.GPIO as GPIO

idSensorAgua=40
idSensorComida=38
idSensorLuz=40

def iniciar_sensores():
    print("iniciando sensores")
    # GPIO.setmode(GPIO.BCM)

def hay_agua():
    return "SIagua"

def hay_comida():
    return "NOcomida"

def estado_luz():
    if(GPIO.input(idSensorLuz)):
        return "prendido"
    else:
        return "apagao"


def finalizar_sensores():
    print("finalizar sensores")


