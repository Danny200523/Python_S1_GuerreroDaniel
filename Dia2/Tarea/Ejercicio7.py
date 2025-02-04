## Ejercicio 7 Daniel Guerrero

n1=int(input("Ingrese el primer numero que quiere saber si es primo: "))
print("")
n2=int(input("Ingrese el segundo numero que quiere saber si es primo: "))
sum1=0
sum2=0
if n1==1:
    sum1=1
else:
    for i in range(1,n1-1):
        if n1%i==0:
            sum1=sum1+i

if n2==1:
    sum2=1
else:
    for i in range(1,n2-1):
        if n2%i==0:
            sum2=sum2+i


if sum1==n2 and sum2==n1:
    print("Los numero son parceritos")
else:
    print("Los numeros no son parceritos")



## Realizado por: Daniel Guerrero