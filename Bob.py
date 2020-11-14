from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    #message = b'test'
    #print('sending {!r}'.format(message))
    #sock.sendall(message)
    # Look for the response
    #amount_received = 0
    #amount_expected = len(message)
    #data = sock.recv(512)
    #amount_received += len(data)
    #print('received {!r}'.format(data))
    #cipher = PKCS1_v1_5.new(key)
    #crypto = cipher.encrypt(message)
    #print(crypto)
    #sock.sendall(crypto)

    data = sock.recv(512)
    key = RSA.importKey(data, passphrase=None)
    print("Llave pública recibida:",key)
    #sock.sendall(b'hola')
finally:
    print('closing socket')
    sock.close()

f1 = open("hashed.txt","r")
f2 = open("encrypted.txt","w")
Lines = f1.readlines()
cipher = PKCS1_OAEP.new(key)

for line in Lines:
    var = line.strip().encode("utf-8")
    crypto = cipher.encrypt(bytes(var))
    print("Mensaje cifrado:",crypto)
    f2.write(str(crypto)+"\n")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)

try:
    sock.sendall(b'encriptado')

finally:
    print('closing socket')
    sock.close()

f1.close()
f2.close()