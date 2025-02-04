##Ejercicio 5: Calculador de IMC
##Crea un programa que calcule el Índice de Masa Corporal (IMC) y clasifique el resultado según las categorías:
##Menos de 18.5: Bajo peso
##18.5 a 24.9: Peso normal
##25 a 29.9: Sobrepeso
##30 o más: Obesidad

peso=float(input("Ingrese su peso en kilogramos "))
altura=float(input("Ingrese su altura en metros "))

rs=peso/altura**2

if rs<=18.5:
    print("el peso es: ",rs," Bajo peso")
elif rs>18.5 and rs<24.9:
    print("El peso es: ",rs," Peso normal")
elif rs>24.9 and rs<29.9:
    print("El peso es: ",rs,"SOBREPESO")
elif rs>29.9:
    print("El peso es: ",rs,"OBESIDAD")