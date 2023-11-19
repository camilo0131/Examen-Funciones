

def suma_pares(i):
    sumpar = 0
    for x in range(0, i+1 ):
     if (x % 2 == 0):
       sumpar += x
    return sumpar
        
i = int(input('ingresar numero :'))
resultado=suma_pares(i)
print(resultado)