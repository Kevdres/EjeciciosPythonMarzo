correctas = int(input("Ingrese numero de respuestas correctas: "))
incorrectas = int(input("Ingrese numero de respuestas incorrectas: "))
total = correctas + incorrectas
pCorrectos = (100/total)*correctas
pIncorrectas = (100/total)*incorrectas
print("Su puntaje final fue: "+str(correctas)+"/"+str(total))
print("Su porcentaje de aciertos es: %.2f Su porcentaje de errores es: %.2f" %(pCorrectos, pIncorrectas))
