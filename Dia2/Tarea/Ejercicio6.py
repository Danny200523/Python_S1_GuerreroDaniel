## Ejercicio 6 Daniel Guerrero

n=int(input("Ingrese la cantidad de empleados que va a registrar: "))
vp=0.04
sueldomenor=1
sueldo=1
sueldomayor=1
eps=0.0
pension=0.0
sueldobruto=0.0
sueldototal=0
sueldobrutototal=0
epstotal=0
pensiontotal=0
for i in range(n):
    nombrempleado=input("Ingrese el nombre del empleado: ")
    horastrabajadas=int(input("Ingrese el numero de horas: "))
    sueldobruto=horastrabajadas*20000
    eps=sueldobruto*vp
    pension=sueldobruto*vp
    sueldoneto=sueldobruto-eps-pension
    sueldototal=sueldoneto+sueldototal
    epstotal=epstotal+eps
    pensiontotal=pensiontotal+pension
    sueldobrutototal=sueldobrutototal+sueldobruto
    print("")
    print("El nombre del empleado es: ",nombrempleado)
    print("")
    print("El sueldo bruto es ",sueldobruto)
    print("")
    print("El sueldo neto es: ",sueldoneto)
    print("")
    print("EL descuento de eps es: ",eps)
    print("")
    print("EL descuento de pension es: ",pension)
    print("")
    sueldomayor=sueldoneto
    if sueldomayor>sueldomenor:
        sa=sueldomayor
        sueldomenor=sueldomayor
        empleado=nombrempleado
    else:
        if sueldomayor<sueldomenor:
            sm=sueldomayor
            empleado2=nombrempleado

promsueldoneto=sueldototal/n
promsueldobruto=sueldobrutototal/n
print("El trabajdor con mas sueldo fue: ",empleado)
print("El sueldo fue: ",sa)
print("")
print("El trabajador con menos sueldo fue: ",empleado2)
print("el sueldo fue: ",sm)
print("")
print("El total de salarios brutos fue: ",sueldobrutototal)
print("")
print("El total de salarios netos fue: ",sueldototal)
print("")
print("El total de descuento de eps es: ",epstotal)
print("")
print("El total de descuento por pension es: ",pensiontotal)
print("")
print("El promedio de salarios netos fue: ",promsueldoneto)
print("")
print("El promedio de los salarios brutos fue: ",promsueldobruto)
print("")

## Realizado por: Daniel Guerrero