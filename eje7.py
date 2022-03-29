from random import randint

zonaUsuario = int(input("¿En que zona desea disparar?: "))
zonaPortero = randint (1,6)

if zonaUsuario == zonaPortero :
    print("El portero cubrio la zona",zonaPortero ,", no se anoto gol")
else:
    print("El portero cubrio la zona",zonaPortero ,", GOL!")