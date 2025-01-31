def tempf (c):
    rs=0.0
    rs=c*1.8+32
    return rs
def tempc (f):
    r=0.0
    r=(f-32)*0.5556
    return r

temperatura=float(input("Ingrese la temperatura de la cual requiera hacer el cambio :happy: "))
opc=input("ingrese que tipo de temperatura es farenheit(f) o celsius(c) ")

if opc=="f":
    print(tempc(temperatura))
else:
    if opc=="c":
        print(tempf(temperatura))