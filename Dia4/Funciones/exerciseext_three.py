##Ejercicio 3: Clasificación de años
##Crea un programa que determine si un año es:
##Bisiesto (divisible entre 4 pero no entre 100, excepto si también es divisible entre 400).
##Común.

año=int(input("Ingrese el año que quiere saber si es bisiesto: "))

if año%4==0:
    if año%100==0:
        if año%400==0:
            print("El año es bisiesto")
        else:
            print("El año no es bisiesto")
    else:
        print("El año es bisiesto")
else:
    print("El año no es bisiesto")