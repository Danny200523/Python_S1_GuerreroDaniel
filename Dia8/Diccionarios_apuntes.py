##DICCIONARIOS
##Los diccionarios en python son una estructura que permite almacenar su contenido
##en forma de llave/valor -- clave/valor. en python, los diccionarios se crean con llaves{}, donde cada par se separa
##con una coma
usuario1={"Nombre":"Pedro",
          "Edad":24,
          "Documento":1049291388}
##Otra opcion para crear diccionarios: usuario2=dict{Nombre="Pedro",Edad=24,Documento=1049291388}


##OBTENER EL NOMBRE
nombreusuario=usuario1["Nombre"]
print(nombreusuario)
print(type(nombreusuario))

##Recorrer un diccionario
for i in usuario1:
    print(i,usuario1[i])

##Hacer un programa que use un diccionario  para gestionar los productos y precios de la tabla,
#pregunte al usuario por un producto y la cantidad. Mostrar por pantalla el precio total.
#si el producto no esta debe mostrar un mensaje informando de ello
productos={
    "menta":300,
    "Chocorramo":1000,
    "esfero":2700,
    "chocolatina":2500,
}
producto=input("¿Que producto deseas?")
cantidad=int(input("¿Cuantos desea?"))
if producto in productos:
    print(cantidad,producto+"s","Vale/n","$",productos[producto]*(cantidad))
else:
    print("sorry, no tenemos eso")