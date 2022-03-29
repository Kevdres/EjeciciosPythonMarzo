saldoCuenta=0
opcion=1
while(opcion!=3):
    opcion = int(input("Ingrese una opcion:\n1.-Retiro \n2.-Deposito \n3.-Salir "))
    if opcion>3 or opcion<1:
        print("ELIJA UN OPCION VALIDA\n")
        continue
    if opcion==1:
        retiro =float(input("Ingrese el valor que desea RETIRAR: "))
        if (saldoCuenta-retiro)<0:
            print("SALDO INSUFICIENTE")
        else:
            saldoCuenta-=retiro

    elif opcion==2:
        saldoCuenta += float(input("Ingrese el valor que desea DEPOSITAR: "))
    elif opcion==3:
        print("SALIENDO")
    print("Saldo Total: ",saldoCuenta,"\n")
   