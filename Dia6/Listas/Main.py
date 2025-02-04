## Listas
## Una lista es una estructura de datos que organiza y 
# almacena de manera secuencial y ordenada

##nombre =["Pedro","Edgar","David"]
##Caracteristicas :
## 1. El tamaño es dinamico, pues se pueden ingresar x datos

nombres=["pedro","edgar","David"]
print(len(nombres))
nombres.append("Aguilar")
print(len(nombres))
##2. para recorrer una lista se utilizan los indices, los cuales
##son la poscision adentro de la lista
print(nombres[2])
##3. En python, las listas pueden almacenar diferentes tipos de datos a la vez
nombres.append(True)
print(nombres)

##Funciones mas comunes 
## Agregar : append() para agregar en la cola
listanueva=[]
listanueva.append("Cajasan")
print(listanueva)

##Extend: permite agregar una lista adicional a una lista existente
lista1=[1,2,3,4,5]
lista1.extend([6,7,8,9,0])
print(lista1)

##Insert en un indice : permite agregar un elemento en una posicion exacta
listaindice=["rojo","azul"]
listaindice.insert(1,"amarillo")
print(listaindice)

##Reemplazar un item en un indice : permite reemplazar un item que esta en un indice en especifico
listareemplazar=["pedro","gomez"]
listareemplazar[1]="Bonilla"
print(listareemplazar)

##Eliminar el ultimo item en cola : para eliminar el ultimo item en cola utilizamos pop()
## sino le ingresamos el indice
listapop=["andres","camargo","david","perez"]
listapop.pop()
print(listapop)
listapop.pop(0)
print(listapop)

##contar elementos: para contar cuantos elementos hay iguales en una lista utilizamos . count()
vocales=["a","e","i","o","u","a"]
apariciones = vocales.count("a")#Retornar el numero de veces que la "a" esta presente en la lista
print(apariciones)

##ORDENAMIENTO
##Con solo numeros
#si quiero ordenar una lista de numeros utilizo .sort()
listanum=[7,4,6,2,8,0]
listanum.sort()##Menos a Mayor
print(listanum)
listanum.sort(reverse=True)#Mayor a Menor
print(listanum)
print("\n###########")
print("\n###########")
##Recorrer una lista
estudiantes = [
    "Adrián Quintero Pinzón",
    "Alejandra Pinzón Alvarez",
    "Ámbar Isabella Plata López",
    "Andrés David Reyes Espinel",
    "Aura Camila Pico Araque",
    "Camilo Andrés Suárez Fuentes",
    "Daniel Esteban Guerrero Quintero",
    "David Santiago Vera Mendez",
    "Edgar Leonardo Acevedo Arteaga",
    "Gerson Steven Chaparro Martínez",
    "Harley Yefrey Cabrales Vargas",
    "John Stiven Negron Regalado",
    "Juan David Saavedra Jaimez",
    "Juan David Santoyo Jaimes",
    "Juan David Vargas Soto",
    "Juan Eduardo Pinilla Guzmán",
    "Juan Fernando Umaña Barragan",
    "Juan Jose Abril Roman",
    "Maria Juliana Saavedra Mejia",
    "Mateo Roman Camargo",
    "Naya Zarela Lizcano Jaimes",
    "Nicolas Chedraui Mantilla",
    "Omar Fernando Granados Parra",
    "Santiago Aguilar Vesga",
    "Santiago Andrés Quiñonez Sosa",
    "Santiago Jaimes Perez",
    "Sara Sofía Díaz Rodríguez",
    "Sayara Yurley Aparicio Arciniegas",
    "Sergio Andrés Rueda Hernández",
    "Simón Dante Salamanca Galvis",
    "Thomas Sebastián Bastos Garcia",
    "Vladimir Diaz Contreras"
]
##Metodo 1: Utilzar un for con indices
for i in range(len(estudiantes)):
    print("Estudiante#",i+1,": ",estudiantes[i])

print("\n###########")
print("\n###########")
##Metodo 2: Recorrerlo con un for que vaya indice por indice
for i in estudiantes:
    print(i) 

