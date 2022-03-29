lista1 = ["a", "b", "c", "d", "e"]
lista2 = ["c", "e", "f", "t", "g"]
listaTodo = []
listSolo1 = []
listSolo2 = []
listAmbas = []

listaTodo = lista1+lista2

for palabra in lista1:
    if palabra in lista2:
        listAmbas += [palabra]
    else:
        listSolo1 += [palabra]

for palabra in lista2:
    if palabra not in lista1:
        listSolo2 += [palabra]
print(lista1)
print(lista2)
print(listaTodo)
print(listSolo1)
print(listSolo2)
print(listAmbas)
