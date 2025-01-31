## triple IZI solo el par o impar
from math import sqrt
def par(n):
    if n%2==0:
        print("el numero es par :happy:")
    else:
        print("el numero no es par :sad:")



## YA NO ES IZI 
def cuadrado_perfecto(n):
    r= int (n**0.5)
    if r*r == n:
        print (n," Es un cuadrado perfecto")
    else:
        print (n," No es un cuadrado perfecto")


r=float(input("Ingrese un numero "))

print(par(r))
print("")
print(cuadrado_perfecto(r))


