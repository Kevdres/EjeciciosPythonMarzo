
dias = int(input("Ingrese numero de dias: "))
anios = dias//365
meses = (dias % 365)//30
semanas = (dias-(anios*365+meses*30))//7
dias2 = dias-(anios*365+meses*30+semanas*7)
print(dias,"equivale a: ",anios,"años,",meses,"meses,",semanas,"semanas y ",dias2,"dias")