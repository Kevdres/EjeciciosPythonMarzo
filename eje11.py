def rangoAnios(anio1, anio2):
    r = "Años entre "+str(anio1)+" y "+str(anio2)+":"
    bisiestos = "Años bisiestos: "
    multiplos = "Multiplos de 10: "
    for i in range(anio1, anio2+1, 1):
        r += str(i)+", "
        if(i % 10 == 0):
            bisiestos += str(i)+", "
        if(i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
            multiplos += str(i)+", "
    print(r)
    print(bisiestos)
    print(multiplos)


rangoAnios(2000, 2022)
