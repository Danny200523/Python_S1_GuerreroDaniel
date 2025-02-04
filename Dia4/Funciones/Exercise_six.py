##Escriba una función para generar la secuencia de Fibonacci hasta una cantidad determinada de términos.
##Modifíquela para que devuelva solo números pares de Fibonacci.
##Extiéndala para encontrar la suma de los números de Fibonacci dentro de un rango especificado.

def fibo(f):
    a=0
    b=1
    for i in range(1,f):
        print(a)
        print(b)
        a=a+b
        b=b+a

def fibopar(r):
    a=0
    b=1
    for i in range(1,r):
        if a%2==0 and b%2==0:
            print(a)
            print(b)
        elif a%2==0:
            print(a)
        elif b%2==0:
            print(b)
        a=a+b
        b=b+a

def sumafibo(c):
    a=0
    b=1
    for i in range(1,c):
        c+=a+b
        a=a+b
        b=b+a
    return c



valor=int(input("Ingrese la cantidad de veces que quiere que se haga la sucesion de fibonacci "))

print("La sucesion de fibonacci es: ")
print(fibo(valor))
print("")
print("La sucesion de fibonacci (solo pares): ")
print(fibopar(valor))
print("")
print("La suma de la serie de fibonacci es: ")
print(sumafibo(valor))