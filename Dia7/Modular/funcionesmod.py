nombres = [
    ["Adrián"],
    ["Alejandra"],
    ["Ámbar", "Isabella"],
    ["Andrés", "David"],
    ["Aura", "Camila"],
    ["Camilo", "Andrés"],
    ["Daniel", "Esteban"],
    ["David", "Santiago"],
    ["Edgar", "Leonardo"],
    ["Gerson", "Steven"],
    ["Harley", "Yefrey"],
    ["John", "Stiven"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "Eduardo"],
    ["Juan", "Fernando"],
    ["Juan", "Jose"],
    ["Maria", "Juliana"],
    ["Mateo", "Roman"],
    ["Naya", "Zarela"],
    ["Nicolas"],
    ["Omar", "Fernando"],
    ["Santiago"],
    ["Santiago", "Andrés"],
    ["Santiago"],
    ["Sara", "Sofía"],
    ["Sayara", "Yurley"],
    ["Sergio", "Andrés"],
    ["Simón", "Dante"],
    ["Thomas", "Sebastián"],
    ["Vladimir"]
]

apellidos = [
    ["Quintero", "Pinzón"],
    ["Pinzón", "Alvarez"],
    ["Plata", "López"],
    ["Reyes", "Espinel"],
    ["Pico", "Araque"],
    ["Suárez", "Fuentes"],
    ["Guerrero", "Quintero"],
    ["Vera", "Mendez"],
    ["Acevedo", "Arteaga"],
    ["Chaparro", "Martínez"],
    ["Cabrales", "Vargas"],
    ["Negron", "Regalado"],
    ["Saavedra", "Jaimez"],
    ["Santoyo", "Jaimes"],
    ["Vargas", "Soto"],
    ["Pinilla", "Guzmán"],
    ["Umaña", "Barragan"],
    ["Abril", "Roman"],
    ["Saavedra", "Mejia"],
    ["Camargo"],
    ["Lizcano", "Jaimes"],
    ["Chedraui", "Mantilla"],
    ["Granados", "Parra"],
    ["Aguilar", "Vesga"],
    ["Quiñonez", "Sosa"],
    ["Jaimes", "Perez"],
    ["Díaz", "Rodríguez"],
    ["Aparicio", "Arciniegas"],
    ["Rueda", "Hernández"],
    ["Salamanca", "Galvis"],
    ["Bastos", "Garcia"],
    ["Diaz", "Contreras"]
]

def opc1():
    nu1vest=input("Ingrese el primer nombre del estudiante")
    nu2vest=input("Ingrese el segundo nombre del estudiante (si aplica)")
    ap1est=input("Igrese el primer apellido del estudiante")
    ap2est=input("Ingrese el segundo apellido del estudiante")
    nombres.append([nu1vest,nu2vest])
    apellidos.append([ap1est,ap2est]) 

def opc2():
    n=0
    n1=0
    for i in range(len(nombres)):
        print("Estudiante#",i+1,": "," ".join(nombres[n])," ".join(apellidos[n1]))
        n+=1
        n1+=1
    n=0
    n1=0

def opc3():
    print("Editar estudiantes")
    opc2()
    est=int(input("Que estudiante quiere editar? (numero de la lista)"))
    est=est-1
    print("1. Editar primer Nombre")
    print("2. Editar segundo Nombre")
    print("3. Editar primer apellido")
    oc=input("4. Editar segundo apellido")
    match oc:
        case "1":
            vr=input("Ingreselo corregido")
            nombres[est][int(oc)-1]=vr
        case "2":
            vr=input("Ingreselo corregido")
            nombres[est][int(oc)-1]=vr
        case "3":
            vr=input("Ingreselo corregido")
            apellidos[est][int(oc)-4]=vr
        case "4":
            vr=input("Ingreselo corregido")
            apellidos[est][int(oc)-3]=vr
        case _:
            print("escribi bien care chimba")

def opc4():
    opc2()
    es=input("ingrese el numero del estudiante que quiere eliminar")
    nombres.pop(int(es)-1)
    apellidos.pop(int(es)-1)

def menu():
    print("Que te gustaría hacer?")
    print("1.Agregar estudiante")
    print("2. Ver estudiantes")
    print("3.Editar estudiante")
    print("4.Eliminar estudiante")
    print("5.Salir del programa")
    print("\nBienvenido al programa de lista de estudiantes\n");b=True
    while b==True:
        opcionUsuario=int(input(":"))
        if opcionUsuario==1:opc1()
        elif opcionUsuario==2:opc2()
        elif opcionUsuario==3:opc3()
        elif opcionUsuario==4:opc4()
        elif opcionUsuario==5:b=False