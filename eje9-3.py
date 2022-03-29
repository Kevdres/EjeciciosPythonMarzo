segundos = 45
minutos = 59
horas = 23

if horas <=23 and minutos <= 59 and segundos <= 59:
    segundos += 1
    if segundos == 60:
        minutos += 1
        segundos = 0
    if minutos == 60:
        minutos = 0
        horas += 1
    if horas == 24:
        horas = 0
else:
    print("Ingrese una hora valida")

print(str(horas)+":"+str(minutos)+":"+str(segundos))
