from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
import rsa
import base64
import socket
import sys
random_generator = Random.new().read

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
key = RSA.generate(1024, random_generator)
sock.listen()

while True:
    enviada = False
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print('connection from', client_address)
        connection.sendall(key.publickey().exportKey(format='PEM', passphrase=None, pkcs=1))
        enviada = True
        # Receive the data in small chunks and retransmit it

    finally:
        # Clean up the connection
        connection.close()
    if enviada:
        print("llave pública enviada, esperando mensajes cifrados.")
        break
    
print("\n")

while True:
    encriptado = False
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        data = connection.recv(512)
        texto = data.decode("utf-8")
        if data:
            if texto == "encriptado":
                encriptado = True
        else:
            print('no data from', client_address)
            print('ending connection')
            break

    finally:
        connection.close()
    if encriptado:
        break

f2 = open("encrypted.txt","r")
Lines = f2.readlines()

for line in Lines:
    cipher = PKCS1_OAEP.new(key)
    var = line.strip()
    print(var,"\n")
    #ciphertext = var.decode("utf-8")
    #print(type(ciphertext))
    #print(ciphertext)
    #msg = cipher.decrypt(ciphertext, sentinel)
    #print("descifrado:",msg)