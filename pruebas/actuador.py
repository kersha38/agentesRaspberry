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
        self.rotador_servo.start(10)

    def abrir_agua(self):
        print("sirviendo agua")
        self.rotador_servo.ChangeDutyCycle(5)
        time.sleep(3)
        self.rotador_servo.ChangeDutyCycle(10)
        time.sleep(1)
        self.rotador_servo.ChangeDutyCycle(0)

    def abrir_comida(self):
        print("sirviendo comida")
        self.rotador_servo.ChangeDutyCycle(10.5)
        time.sleep(1)
        self.rotador_servo.ChangeDutyCycle(7.5)

    def finalizar_actuadores(self):
        print("finalizar actuadores")
        self.rotador_servo
        self.rotador_servo.stop()
        GPIO.cleanup(self.idServo)
