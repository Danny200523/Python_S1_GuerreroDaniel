##||||||||||||||||||||||||||||||||||||||||||||||
##||||||||||||||CALCULADORA|||||||||||||||||||||
##||||||||||||||||||||||||||||||||||||||||||||||

n=float(input("ingrese el primer numero a hacer la operacion"))
n2=float(input("ingrese el segundo numero a hacer la operacion"))
ope=str(input("ingrese el tipo de operacion basica que quierer realizar(+, -, *, /)"))

if ope=="+":
    rs=n+n2
    print("El resultado es",rs)

if ope=="-":
    rs=n-n2
    print("El resultado es",rs)

if ope=="*":
    rs=n*n2
    print("El resultado es",rs)

if ope=="/":
    rs=n/n2
    print("El resultado es",rs)