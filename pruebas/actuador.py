import RPi.GPIO as GPIO
import time


class Actuador:
    def __init__(self):
        print('inicializando actuadores')
        self.idServo = 35
        self.rotador_servo = 1
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.idServo, GPIO.OUT)
        self.rotador_servo = GPIO.PWM(self.idServo, 50)
        self.rotador_servo.start(7.5)

    def abrir_agua(self, tiempoAgua):
        print("sirviendo agua")
        self.rotador_servo.ChangeDutyCycle(4.5)
        time.sleep(tiempoAgua)
        self.rotador_servo.ChangeDutyCycle(7.5)

    def abrir_comida(self, tiempoComida):
        print("sirviendo comida")
        self.rotador_servo.ChangeDutyCycle(10.5)
        time.sleep(tiempoComida)
        self.rotador_servo.ChangeDutyCycle(7.5)

    def finalizar_actuadores(self):
        print("finalizar actuadores")
        self.rotador_servo
        self.rotador_servo.stop()
        GPIO.cleanup(self.idServo)
