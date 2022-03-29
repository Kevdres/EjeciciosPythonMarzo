frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
cont = 0

for carac in frase:
    if carac == letra:
        cont += 1
if cont>0:
    print("La letra "+letra+" esta "+str(cont)+" veces")
else: 
    print("No se encontro la letra "+letra)


# for i in range(len(frase)):
#     if frase[i]==letra:
#         cont+=1
# print("La letra esta "+str(cont)+" veces")
