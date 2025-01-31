## Ejercicio 4 Daniel Guerrero

grande=0
menor=5
for i in range (10):
    N=int(input("Ingrese el numero: "))
    if N>grande:
        grande=N
    else:
        if N<menor:
            menor=N

print("El numero menor es: ",menor)
print("")
print("El numero mayor es: ",grande)

##Realizado por: Daniel Guerrero