def Imprimir(dic):
    for indice in dic:
        print("Key:", indice, "Value:", dic[indice])


def AgregarEstudiante(dic, codigo, nombre):
    dic[codigo] = []
    dic[codigo].append(nombre)
    dic[codigo].append([])


def AgregarNota(dic, codigo, nota):
    dic[codigo][1] += [nota]


def Promedio(lista):
    suma = 0
    for item in lista:
        suma += item
    return suma/len(lista)


dic = {}
Imprimir(dic)
AgregarEstudiante(dic, "001", "Kevin")
AgregarNota(dic, "001", 10)
AgregarNota(dic, "001", 8)
Imprimir(dic)
print(Promedio(dic["001"][1]))
