def opc1(a,b):
    nu1vest=input("Ingrese el primer nombre del estudiante")
    nu2vest=input("Ingrese el segundo nombre del estudiante (si aplica)")
    ap1est=input("Igrese el primer apellido del estudiante")
    ap2est=input("Ingrese el segundo apellido del estudiante")
    a.append([nu1vest,nu2vest])
    b.append([ap1est,ap2est]) 

def opc2(a,b):
    n=0
    n1=0
    for i in range(len(a)):
        print("Estudiante#",i+1,": "," ".join(a[n])," ".join(b[n1]))
        n+=1
        n1+=1
    n=0
    n1=0

def opc3(a,b):
    print("Editar estudiantes")
    opc2(a,b)
    est=int(input("Que estudiante quiere editar? (numero de la lista)"))
    est=est-1
    print("1. Editar primer Nombre")
    print("2. Editar segundo Nombre")
    print("3. Editar primer apellido")
    oc=input("4. Editar segundo apellido")
    match oc:
        case "1":
            vr=input("Ingreselo corregido")
            a[est][int(oc)-1]=vr
        case "2":
            vr=input("Ingreselo corregido")
            a[est][int(oc)-1]=vr
        case "3":
            vr=input("Ingreselo corregido")
            b[est][int(oc)-4]=vr
        case "4":
            vr=input("Ingreselo corregido")
            b[est][int(oc)-3]=vr
        case _:
            print("escribi bien care chimba")

def opc4(a,b):
    opc2(a,b)
    es=input("ingrese el numero del estudiante que quiere eliminar")
    a.pop(int(es)-1)
    b.pop(int(es)-1)
