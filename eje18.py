from random import randint
operacion = randint(1, 2)
correcta = True
aciertos = 0
while (correcta == True):

    if(operacion == 1):
        n1 = randint(1, 10)
        n2 = randint(1, 10)
        resultado = n1*n2
        print(n1, "*",n2, "= ")
        resultadoUsuario = int(input("Ingrese su respuesta: "))
        if resultadoUsuario == resultado:
            aciertos += 1
            print("Respuesta Correcta")
        else:
            correcta == False
            print("Respuesta Inorrecta")

    elif(operacion == 2):
        n1 = randint(1, 10)
        n2 = randint(1, 10)
        resultado = n1//n2
        print(n1, "/",n2, "= ")
        resultadoUsuario = int(input("Ingrese su respuesta: "))
        if resultadoUsuario == resultado:
            aciertos += 1
            print("Respuesta Correcta")
        else:
            correcta == False
            print("Respuesta Inorrecta")
print("Total de aciertos: ", aciertos)
