lista = [1, "hola", 3.5, False]

while len(lista)>0:
    print(lista)
    elem=int(input("Ingrese la psicion del elemento a eliminar: "))
    if elem>len(lista)-1:
        print("El elemento esta fuera de rango")
        continue
    del(lista[elem])
    print()