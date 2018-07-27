import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(29,GPIO.IN)#,pull_up_down=GPIO.PUD_UP)

try:
    while(True):
        print("midiento")
        print(GPIO.input(29))
        time.sleep(1)
finally:
    GPIO.cleanup()
