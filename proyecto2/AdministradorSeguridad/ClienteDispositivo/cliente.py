import socket, ssl, pprint, base64, msgpack

# Comandos para generar las llaves y los certificados uto-firmados:

# - Genera la llave privada del servidor (server.key): 
# openssl genrsa -out server.orig.key 2048
# openssl rsa -in server.orig.key -out server.key

# - Genera la peticion de certificacion (server.csr):
# openssl req -new -key server.key -out server.csr

# - Genera el ceritifcado del servidor (server.crt):
# openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt


# Constantes del host y puertos a usar:
p_host = "AdministradorSeguridad.mascotsens.co"
p_hostname = "AdminSeguridad.mascotsens.co"
p_port = 10023
# Ubicacion del certificado del servidor: -----> No es necesario
# ssl_server_cert = "/home/centos/Downloads/AdminSeguridad.crt"

# Ruta donde se encuentra el archivo .csr a leer:
csr_route = "/home/centos/Downloads/certificados/real.csr"
# Ruta donde se encuentra el id de fabrica del dispositivo:
txt_route = "/home/centos/Downloads/certificados/falso.txt"
#Id del dispositivo
id_disp = "563gjht89"
# String que guardara todo el contenido del archivo csr:
csr_content = ""
# String que guardara todo el contenido del archivo txt:
txt_content = ""

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.load_default_certs()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# La conexion require el certificado del servidor. Por ahora se usa el auto-firmado

ssl_sock = context.wrap_socket(s, server_hostname=p_hostname)
# Anterior ----->
# ssl_sock = ssl.wrap_socket(s,
#                           ca_certs=ssl_server_cert,
#                           cert_reqs=ssl.CERT_REQUIRED)


ssl_sock.connect((p_host, p_port))

# ---> Control del socket
# print repr(ssl_sock.getpeername())
# print ssl_sock.cipher()
# print pprint.pformat(ssl_sock.getpeercert())


# ---> Lee el archivo .csr y su contenido lo asigna a un solo string:
# Abre el archivo:
csr_file = open(csr_route, 'r')

# Recorre su contenido:
for line in csr_file:
	csr_content+= line
	# -->

# Transforma el string a base64 para evitar errores de transmision(?)
# b64_csr_string = base64.b64encode(csr_content)

# Abre el archivo txt:
txt_file = open(txt_route, 'r')

# Recorre su contenido:
for line in txt_file:
	txt_content+= line
	# -->


# Transforma el string a base64 para evitar errores de transmision(?)
# b64_txt_string = base64.b64encode(txt_content)

msgPack = [csr_content, txt_content, id_disp]

packed = msgpack.packb(msgPack)

# Codifica el paquete:
codedPack = base64.b64encode(packed)

# Envia al servidor el contenido de ambos archivos como un paquete:
# TO-DO: ssl_sock.write(codePack)
ssl_sock.write(codedPack)

# ------ Ejemplo ------------
#if False: # from the Python 2.7.3 docs
#    # Set a simple HTTP request -- use httplib in actual code.
#    ssl_sock.write("""GET / HTTP/1.0\r
#    Host: www.verisign.com\n\n""")
#
#    # Read a chunk of data.  Will not necessarily
#    # read all the data returned by the server.
#    data = ssl_sock.read()
#
#    # note that closing the SSLSocket will also close the underlying socket
#    ssl_sock.close()

