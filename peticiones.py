import requests

fileAgua=open("fileagua.txt","r")
cantidadAgua=float(fileAgua.read())
fileAgua.close()

fileComida=open("filecomida.txt","r")
cantidadComida=float(fileComida.read())
fileComida.close()

def obtener_mac(interface='eth0'):
    try:
        str = open('/sys/class/net/%s/address' % interface).read()
    except:
        str = "00:00:00:00:00:00"
    return str[0:17]

raspberry=str(obtener_mac())

direccion_base = 'https://tranquil-mountain-87492.herokuapp.com/'
#direccion_base = 'http://192.168.5.10:300/'

def consultar_orden():
    orden_actual = requests.get(direccion_base + 'Raspberry/obtenerOrden?raspberry=' + raspberry)

    try:
        return (orden_actual.json()["tipo"])
    except:
        return ("sin orden")

def actualizar_senso(senso):
    requests.get(direccion_base
                 +'Raspberry/actualizarSenso?raspberry='
                 + raspberry
                 + '&&estado='
                 + senso)
    print (senso)

def subirArchivo():
    with open('bati.PNG', 'rb') as file:
        r = requests.post(direccion_base
                          +'Raspberry/subirVideo',
                          files={'file': file})

def publicarRaspberry():
    requests.get(direccion_base+'Raspberry/publicarRaspberry?raspberry='+raspberry)

def publicarIP():
    requests.get(direccion_base+'Raspberry/publicarIP?raspberry='+raspberry)

def actualizarConfiguracion():
    configuracion = requests.get(direccion_base+'Raspberry/consultarConfiguracion?raspberry='+raspberry)
    global cantidadAgua
    global cantidadComida

    cantidadAgua = float(configuracion.json()['cantidadAgua'])
    cantidadComida = float(configuracion.json()['cantidadComida'])
    fileAgua=open("fileagua.txt","w")
    fileAgua.write(str(cantidadAgua))
    fileAgua.close()
    fileComida=open("filecomida.txt","w")
    fileComida.write(str(cantidadComida))
    fileComida.close()

def getTiempoAgua():
    return cantidadAgua*3/100

def getTiempoComida():
    return cantidadComida*3/100

