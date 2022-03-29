listaPesoHumanos = [80, 34, 80, 23, 70]
sumaAlta = 0
contador = 0
for i in range (len(listaPesoHumanos)):
    for j in range(i+1, len(listaPesoHumanos)):
        suma = listaPesoHumanos[i]+listaPesoHumanos[j]
        if (suma <= 150):
            if suma > sumaAlta:
                sumaAlta = suma
            print(contador+1, "-", listaPesoHumanos[i], "+", listaPesoHumanos[j], "=", suma)
            contador += 1

print("El peso maximo posible es: ", sumaAlta)
