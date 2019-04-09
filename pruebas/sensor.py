import RPi.GPIO as GPIO
import time

idSensorAgua = 31
idSensorComida = 29
idSensorLuz = 40
class sensor:
    def __init__(self):
        print("iniciando sensores")
        # GPIO.setmode(GPIO.BOARD)
        GPIO.setup(idSensorComida, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(idSensorAgua, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def hay_agua(self):
        if GPIO.input(idSensorAgua):
            return "SI"
        else:
            return "NO"

    def hay_comida(self):
        if GPIO.input(idSensorComida):
            return "SI"
        else:
            return "NO"

    def estado_luz(self):
        if GPIO.input(idSensorLuz):
            return "SI"
        else:
            return "NO"

    def finalizar_sensores(self):
        print("finalizar sensores")

    def obtener_hora(self):
        return time.strftime("%H:%M:%S")

    def obtener_fecha(self):
        return time.strftime("%d/%m/%y")


