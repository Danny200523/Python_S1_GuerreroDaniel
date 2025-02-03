import random

dictionary={
    "A":"A",
    "B":"B"

}

characterss={
    "+":"+",
    "-":"-",
    "/":"/",
    "*":"*",    
}

number=random.randint(0,9)
numb=random.choice(list(dictionary))
character=random.choice(list(characterss))

print(number,numb,character)
