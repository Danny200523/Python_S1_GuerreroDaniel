##Ejercicio 1: Sistema de recomendaciones de comida
##Escribe un programa que recomiende una comida según el clima
##  (soleado, lluvioso, frío) y la hora del día (mañana, tarde, noche). 
## Usa match para manejar el clima y if para la hora.
day=str(input("Ingrese el clima para recomendarle la comida(soleado, lluvioso, frio)"))
hour=str(input("Ingrese la hora (mañana, tarde, noche)"))
match day:
    case "soleado":
        if hour=="mañana":
            print("El plato recomendado es: Empanada mixta con limonada fria")
        elif hour=="tarde":
            print("El plato recomendado es: Bandeja paisa con jugo natural + postre del gusto")
        else:
            print("El plato recomendado es: pan de queso con chocolisto")
    case "lluvioso":
        if hour=="mañana":
            print("El plato recomendado es: Arepa rellena con chocolate caliente")
        elif hour=="tarde":
            print("El plato recomendado es: Mute con arroz blanco con jugo de lulo")
        else:
            print("El plato recomendado es: sandwich con cafe caliente")
    case "frio":
        if hour=="mañana":
            print("El plato recomendado es: Changua con arepa de maiz")
        elif hour=="tarde":
            print("El plato recomendado es: sancocho trifacico")
        else:
            print("El plato recomendado es: arepa con queso rayado y cafe caliente")
    case _:
        print("El tipo de clima no fue identificado")