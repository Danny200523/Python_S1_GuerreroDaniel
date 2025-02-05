from funcionesmod import *
print("\nBienvenido al programa de lista de estudiantes\n");b=True
while b==True:
    menu();opcionUsuario=int(input(":"))
    if opcionUsuario==1:opc1()
    elif opcionUsuario==2:opc2()
    elif opcionUsuario==3:opc3()
    elif opcionUsuario==4:opc4()
    elif opcionUsuario==5:b=False