
def vasos(n, x):
    total=0
    while(n>=x):
        reciclados = n//x
        sobran = n % x
        total+=reciclados
        n=reciclados+sobran
        print("N:",n,"Reciclado:",reciclados,"sobran",sobran,"total reciclados",total)
    return total

n = 10
x = 4
print(vasos(n, x))
