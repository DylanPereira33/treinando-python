from random import randint

while True:       
    comando = input("Digite qualquer dado ")       

    test = comando
    result = test.split("d")
    result1 = result[1].split("+")
    mult = 1
    if (len(result1) == 1):
        result1 = result[1].split("-")
        mult=-1

    sum = 0
    if (len(result1) == 2):
        sum = result1[1]

    faces = result1[0]
    dados = result[0]
    for i in result[0]:
        aleatorio = randint(1,faces)
        total = sum(int(aleatorio))
    print(total)

