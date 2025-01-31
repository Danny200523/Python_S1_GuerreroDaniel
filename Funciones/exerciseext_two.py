##Ejercicio 2: Conversor de unidades
##Escribe un programa que convierta entre las siguientes unidades:
##Kilómetros a millas
##Celsius a Fahrenheit
##Kilogramos a libras
##Utiliza match para elegir la conversión y if para verificar valores negativos.

tipo=int(input("Ingrese la conversion que quiere hacer"
               "(1) Kilometros a millas"
               "(2) Celsius a Fahrenheit"
               "(3) Kilogramos a libras"))

valor=float(input("Ingrese el valor al que le quiere hacer el cambio"))

rs=0

match tipo:
    case 1:
        if valor<0:
            print("no es posible meter datos negativos")
        else:
            rs=valor/1.6
        print("Los kilometros a millas son: ",rs)
    case 2:        
        if valor<0:
            print("no es posible meter datos negativos")
        else:
            rs=valor*9/5+32
        print("la temperatura fahrenheit: ",rs)
    case 3:        
        if valor<0:
            print("no es posible meter datos negativos")
        else:
            rs=valor*2
        print("Las libras son: ",rs)
    case _:
        print("Conversion no reconocida")