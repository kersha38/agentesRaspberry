import threading
import peticiones
import actuador
import sensor
import RPi.GPIO as GPIO

def empezar_hilos(arr_hilos):
    for hilo in arr_hilos:
        hilo.start()

def actuar():
    try:
        while True:
            realizar_orden(peticiones.consultar_orden())
    finally:
        actuador.finalizar_actuadores()

def sensar():
    try:
        while True:
            senso = '{agua:\'' + sensor.hay_agua() \
                    + "\',comida:\'" + sensor.hay_comida() \
                    + "\',luz:\'" +sensor.estado_luz() + '\'}'
            peticiones.actualizar_senso(senso)
    finally:
        sensor.finalizar_sensores()

def realizar_orden(orden):
    if orden == "agua":
        actuador.abrir_agua()
    elif orden == "comida":
        actuador.abrir_comida()
    elif orden == "luzON":
        actuador.encender_luz()
    elif orden == "luzOFF":
        actuador.apagar_luz()
    else:
        print("ninguna orden")
        
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
hilos = []
peticiones.publicarRaspberry()
peticiones.publicarIP()
sensor.iniciar_sensores()
actuador.iniciar_actuadores()
hilo_actuar = threading.Thread(target=actuar, args=())
hilos.append(hilo_actuar)
hiloSensar = threading.Thread(target=sensar, args=())
hilos.append(hiloSensar)
empezar_hilos(hilos)
