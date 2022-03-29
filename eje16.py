from random import randint

def ppt(opcion):
    if opcion==1:
        r="piedra"
    elif opcion==2:
        r="papel"
    elif opcion==3:
        r="tijera"
    return r


victorias = 0
while(victorias < 3):
    opUsuario = int(
        input("Ingrese una opcion:\n1.-Piedra \n2.-Papel \n3.-Tijera "))
    if opUsuario>3 or opUsuario<1:
        continue
    opMaquina = randint(1, 3)
    print("La maquina eligio:", ppt(opMaquina))
    print("El usuario eligio:", ppt(opUsuario))

    if (opUsuario == 1 and opMaquina == 3) or (opUsuario == 2 and opMaquina == 1) or (opUsuario == 3 and opMaquina == 2):
        print("Gana el Usuario")
        victorias += 1
    elif opUsuario == opMaquina:
        print("Empate")
    else:
        print("Gana la maquina")
    print("VICTORIAS: ", victorias,"\n")
    if (victorias == 3):
        print("JUEGO TERMINADO - VICTORIAS: ", victorias)
