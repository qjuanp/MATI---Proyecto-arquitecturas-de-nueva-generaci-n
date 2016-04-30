import socket, ssl
import base64
from base64 import b64decode
import msgpack
from Crypto.Util.asn1 import DerSequence
from Crypto.PublicKey import RSA
from binascii import a2b_base64
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA512
from Crypto import Random
import sys, getopt
import subprocess
import time

# Constantes del puerto a usar:
p_port = 10023
# Ubicacion del certificado del servidor:
ssl_server_cert = "C:\Llaves\AdminSeguridad.crt"
# Ubicacion de la llave privada del servidor:
ssl_server_key = "C:\Llaves\AdminSeguridad.key"
#Carpeta donde se guardan los csr
folder = "C:\Certitemp\\"

bindsocket = socket.socket()
bindsocket.bind(('', p_port))
bindsocket.listen(5)

def requerimiento_adicional(data):
    mensajeCifradoNoB64 = base64.b64decode(data)
    unpacked = msgpack.unpackb(mensajeCifradoNoB64)
    certificado = unpacked[0]
    idFabrica = unpacked[1]
    idDispositivo = unpacked[2]
    rutaCertificado = folder + idDispositivo + ".csr"
    archivo = open(rutaCertificado, 'w')
    archivo.write(certificado)
    archivo.close()
    # Importa la llave privada
    fkey = open('C:\Llaves\AdminSeguridad.key', 'r')
    private = RSA.importKey(fkey.read())
    fkey.close()

    #Convertir PEM a DER
    fcert = open('C:\Llaves\AdminSeguridad.crt', 'r')
    scert = fcert.read()
    lines = scert.replace(" ",'').split()
    der = a2b_base64(''.join(lines[1:-1]))

    #Extraer la llave publica
    cert = DerSequence()
    cert.decode(der)
    tbsCertificate = DerSequence()
    tbsCertificate.decode(cert[0])
    subjectPublicKeyInfo = tbsCertificate[6]

    #Inicializa la llave RSA
    public = RSA.importKey(subjectPublicKeyInfo)
    fcert.close()

    #Revierte el cifrado en base 64 para poderlo descifrar
    mensajeCifradoNoB64 = base64.b64decode(idFabrica)
    idDesempaquetado = msgpack.unpackb(mensajeCifradoNoB64)
    #Descifrado con llave privada por partes y la guarda en mensajeDescifradoB64
    cipherPrivate = PKCS1_v1_5.new(private)
    mensajeDescifradoB64 = ""
    sentinel = Random.new().read(2)
    for i in range(0, len(idDesempaquetado)):
        mensajeDescifradoActual = cipherPrivate.decrypt(idDesempaquetado[i],sentinel)
        mensajeDescifradoB64 += mensajeDescifradoActual
    mensajeDescifradoPu = base64.b64decode(mensajeDescifradoB64)
    mensajeDescifrado = msgpack.unpackb(mensajeDescifradoPu)
    #Verificacion de firma
    hashPublic = SHA512.new(mensajeDescifrado[0])
    verifier = PKCS1_PSS.new(public)
    mensajeTextoClaro = mensajeDescifrado[0]
    resultado = verifier.verify(hashPublic,mensajeDescifrado[1])

    if resultado:
        comando = 'C:\Scripts\certgen.bat ' + idDispositivo
        proceso = subprocess.Popen(comando, shell = True)
        proceso.communicate()
        rutaCertificadoGenerado = folder + idDispositivo + ".crt"
        certificadoGenerado = open(rutaCertificadoGenerado,'r')
        certResp = ""
        for line in certificadoGenerado:
            certResp += line
        print "Certificado generado correctamente, puede encontrarla con su cadena de certificacion en: C:\Certitemp"
        return certResp
    else:
        print "El dispositivo no esta autorizado por MascotSens"
        return "no autorizado"
    

def atender_cliente(connstream):
    data = connstream.read()
    rdata = data
    print "Recibiendo datos del cliente..."
    tiempoInicio = round(time.time() * 1000)
    i= 0
    while data:
        data = connstream.read()
        rdata+=data
    print rdata
    print "salio"
    return requerimiento_adicional(rdata)
	

while True:
    newsocket, fromaddr = bindsocket.accept()
    connstream = ssl.wrap_socket(newsocket,
                                 server_side=True,
                                 certfile=ssl_server_cert,
                                 keyfile=ssl_server_key)
    try:
        respuesta = atender_cliente(connstream)
        connstream.write(str(respuesta))
    finally:
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()