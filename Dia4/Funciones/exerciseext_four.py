##Ejercicio 4: Conversor de monedas
##Crea un programa que convierta un monto en dólares a otra moneda. Usa las siguientes tasas de cambio:
##Euros: 0.85
##Pesos Colombianos: 4100
##Yenes: 110

cb=float(input("Ingrese que tipo de cambio quiere hacer de dolar a: "
                  "(1) Euros"
                  "(2) Pesos colombianos"
                  "(3) Yenes "
                  ))
valor=float(input("Ingrese la cantidad de dolares a convertir: "))

Euros=0.85
PesosColombianos=4100
Yenes=110

match cb:
    case 1:
        rs=valor*Euros
        print("El valor en euros es: ",rs)
    case 2:
        rs=valor*PesosColombianos
        print("El valor en pesos colombianos es: ",rs)
    case 3:
        rs=valor*Yenes
        print("El valor en yenes es: ",rs)
    case _:
        print("El tipo de cambio no fue identificado")
