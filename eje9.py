a=float(input("Ingrese el valor de a:"))
b=float(input("Ingrese el valor de b:"))

print("La ecuacion es: "+str(a)+" x + "+str(b)+" = 0")

if a==0==b:
    resultado="Todos los numeros son solucion"
elif a==0:
    resultado="No existe solucion"
else:
    resultado="La unica solucion es: "+str(-b /a)
print(resultado)