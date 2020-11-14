import sys
import hashlib

#comandos utilizados para el crackeo de los distintos archivos mediante HashCat 6.1.1
#para medir el tiempo se utilizó el comando Measure-Command {<línea de código>}
#archivo_1: hashcat -a 0 -m 0 archivo_1 diccionario_2.dict
#archivo_2: hashcat -a 0 -m 10 archivo_2 diccionario_2.dict
#archivo_3: hashcat -a 0 -m 10 archivo_3 diccionario_2.dict
#archivo_4: hashcat -a 0 -m 1000 archivo_4 diccionario_2.dict
#archivo_5: hashcat -a 0 -m 1800 archivo_5 diccionario_2.dict


var1 ="Test"
encoded_var1 = var1.encode()
obj_sha3_256 = hashlib.sha3_256(encoded_var1)
print("\nSHA3-256 Hash: ", obj_sha3_256.hexdigest())

f = open("cracked.txt", "r")
f2 = open("hashed.txt", "w")
Lines = f.readlines()

for line in Lines:
    var = line.strip()
    encoded_var = var.encode()
    obj_sha3_256 = hashlib.sha3_256(encoded_var)
    f2.write(obj_sha3_256.hexdigest()+"\n")

print("done")