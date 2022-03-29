numero = int(input("Ingrese un numero: "))
for i in range(1, (numero+1), 1):
    if i % 3 == 0 and i % 5 == 0:       
        print(f"{i} FizzBuzz")
    elif i % 5 == 0:
        print(f"{i} Buzz")
    elif i % 3 == 0:
        print(f"{i} Fizz")
