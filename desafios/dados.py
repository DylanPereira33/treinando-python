# 3d6+2
# sum = 10
# '[5, 1, 2] + 2 = 10'

# 4d2+1
# sum = 10
# '[1, 1, 2, 1] + 1 = 6'

from random import randint

print("""Bem-vindo ao rolador de dados.
      Escreva um dado para rolar seguindo o exemplo: 3d6+5""")

class Rolagem:
    def __init__(self, faces, quantidade = 1, bonus = 0):
        self.qtd   = quantidade
        self.faces = faces
        self.bonus = bonus
        self.rolls = []
   
    def roll(self):
        for _ in range(self.qtd):
            self.rolls.append((randint(1,self.faces)))

        if self.bonus < 0:
            print(f"{self.rolls}{self.bonus} = {sum(self.rolls) + self.bonus}")
        elif self.bonus > 0:
            print(f"{self.rolls} + {self.bonus} = {sum(self.rolls) + self.bonus}")
        else:
            print(f"{self.rolls} = {sum(self.rolls) + self.bonus}")
 
def getData(command):
    loc_d = command.find("d")
    if loc_d == -1:
        raise Exception("formato incorreto")

    bonus = 0
    loc_s = command.find("+")
    if loc_s == -1:
        loc_s = command.find("-")

    if loc_s != -1:
        bonus = int(command[loc_s:])
        faces = int(command[loc_d+1:loc_s])
    else:
        faces = int(command[loc_d+1:])


    qtd = 1
    if command[0] != "d":
        qtd = int(command[:loc_d])
    return (qtd, faces, bonus)


while True:
    (qtd, faces, bonus) = (0, 0, 0)
    command = input("roll: ")
    if command == '':
        break

    (qtd, faces, bonus) = getData(command)

    rolagem = Rolagem(faces, qtd, bonus)
    rolagem.roll()

print("Fim do programa.")