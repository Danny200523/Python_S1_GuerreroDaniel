## Desarrollado por: Daniel Guerrero / T.I 666666666

##/////////////////////////////////
## -- FUNDAMENTOS DE PROGRAMACION
##/////////////////////////////////


##Tipos de Datos
##1. String ""
cadenadetexto="textico"
print (type(cadenadetexto))

##2. Numero Entero -- Int
numeroenter=2
print(type(numeroenter))

##3. Numero FLotante -- float
numeroflotante=1.1
print(type(numeroflotante))

##4. Numero doble -- Double
numerodoble=3.145453684576474675745
print(type(numerodoble))

##5 Booleano -- True/False
booleanito=True
print(type(booleanito))

##Entrada por parte del usuario

x=input("Ingrese un numero:")
print(type(x))

##Entrada por parte del usuario 
## Sintazis - Tipo de dato(dato a convertir)

x=int (input("Ingrese un numero"))
print(type(x))

##Ejercicio - Sumar dos Numeros por parte del usuario
num1=int(input("ingrese un numero para sumarlo "))
num2=int(input("ingrese el siguiente numero "))
resultadossumatorio=num1+num2
print("EL resultado dado es de: ",resultadossumatorio)

## CICLOS FOR Y WHILE
## CICLO FOR NORMAL

for i in range (5):
    print(i)

## Ciclo desde hasta
print("##############")
for i in range(0,5):
    print (i)

##CICLO CON PASOS
print("##############")
for i in range(0,5,2):
    print (i)

##CICLO WHILE 
booleanito1=True
while(booleanito1 == True):
    print(booleanito1)
    booleanito1=False

## /// 4. tipos de FUNCIONES ///

## Funcion SIN PARAMTEROS Y SIN RETORNOS
def funcion1():
    print("Soy una funcion increible")

funcion1()

## FUNCION SIN PARAMETROS PERO CON RETORNO

def funcion2():
    return 5
print("Su numero es: ",funcion2)

## FUNCION CON PARAMETROS Y CON RETORNO
def funcion3(nombre, apellido):
    print("Su nombre es: ",nombre," ",apellido)

funcion3(Daniel, Guerrero)

## FUNCION CON PARAMETROS Y SIN RETORNO
def funcion4(a,b):
    c=a**b
    return c
funcionA=int(input("ingrese el numero base"))
FuncionB=int(input("ingrese la elevacion deseada: "))
print("El resultado de su elevacion es de: ", funcion4(funcionA, FuncionB))

## Desarrollado por: Daniel Guerrero / T.I 666666666