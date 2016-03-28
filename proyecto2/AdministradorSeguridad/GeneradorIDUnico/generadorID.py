from Crypto.Util.asn1 import DerSequence
from Crypto.PublicKey import RSA
from binascii import a2b_base64
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA512
import base64
from base64 import b64decode
from Crypto import Random
import msgpack
import sys, getopt

if len(sys.argv) < 3:
	print "Faltan argumentos, debe especificar el numero unico del dispositivo y el archivo que se genera"
	sys.exit()

archivo = open(sys.argv[2], 'w')
idDispositivo = sys.argv[1]
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

#Firma del mensaje
hashPrivate = SHA512.new(idDispositivo)
signer = PKCS1_PSS.new(private)
signature = signer.sign(hashPrivate)

#Une el id con su firma
mensajeYFirma = [idDispositivo,signature]
#print mensajeYFirma
#Convierte el id con su firma a base64 para que pueda ser cifrado como string

empaquetadoPr = msgpack.packb(mensajeYFirma)
mensajeYFirmaB64 = base64.b64encode(empaquetadoPr)
#Cifrado con llave publica
tamanhoLlavePrivada = ((private.size() + 1) / 8) - 11
tamanhoMensaje = len(mensajeYFirmaB64)
cantidadMensajes = tamanhoMensaje/tamanhoLlavePrivada
mensajeCifrado = []
cipherPublic = PKCS1_v1_5.new(public)
#Se parte el mensaje en partes iguales a las que puede cifrar la llave
for i in range(0, cantidadMensajes):
	inicioString = i * tamanhoLlavePrivada
	finString = ((i+1) * tamanhoLlavePrivada)
	mensajeCifradoActual = cipherPublic.encrypt(mensajeYFirmaB64[inicioString:finString])
	mensajeCifrado.append(mensajeCifradoActual)
	
if tamanhoMensaje%tamanhoLlavePrivada != 0:
	inicioString = cantidadMensajes * tamanhoLlavePrivada
	mensajeCifradoActual = cipherPublic.encrypt(mensajeYFirmaB64[inicioString:])
	mensajeCifrado.append(mensajeCifradoActual)

#Id del dispositivo a guardar en el dispositivo en base64

idEmpaquetado = msgpack.packb(mensajeCifrado)
mensajeCifradoB64 = base64.b64encode(idEmpaquetado)

archivo.write(mensajeCifradoB64)
archivo.close()
print "Archivo generado con nombre: " + sys.argv[1]