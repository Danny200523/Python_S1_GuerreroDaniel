##Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
##Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5
import json
def abrirJSON():
    dicFinal={}
    with open('./bsdt_dcc.json','r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./bsdt_dcc.json",'w') as outFile:
        json.dump(dic,outFile)

inmuebles={}
b=True
while b:
    c=0
    inmuebles=abrirJSON()
    x=int(input("(1). USUARIO O (2). INMOBILIARIA"))
    match x:
        case 1:
            for i in range(len(inmuebles)):
                print("Inmueble#",i+1,": ",inmuebles[c]["año"])
                c+=1
        case 2:
            print("")