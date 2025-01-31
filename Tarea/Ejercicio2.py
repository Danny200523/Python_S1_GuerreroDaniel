## EJERCICIO 2 Daniel Guerrero 

N=int(input("Ingrese la cantidad de terminos que desee: "))
sum=0.0
for i in range (1,N):
    if i%2==1:
        sum=sum+(1/i)
    else:
        if i%2==0:
            sum=sum-(1/i)

print("La cantidad de terminos es: ",N)
print("")
print("El resultado de la operacion es: ",sum)

## Realizado por: Daniel Guerrero