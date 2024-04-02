from random import randint

class Roll:
    def __init__(self):
        self.qtd = 0
        self.faces = 0
        self.bonus = 0
        self.rolls = []
    
    def roll(self):
        if self.qtd == 0:
            print("É preciso pegar o input dos dados do usuário.")
            return
        for _ in range(self.qtd):
            self.rolls.append(int(randint(1,self.faces)))

            if self.bonus < 0:
                print(f"{self.rolls}{self.bonus} = {sum(self.rolls) + self.bonus}")
            elif self.bonus > 0:
                print(f"{self.rolls} + {self.bonus} = {sum(self.rolls) + self.bonus}")
            else:
                print(f"{self.rolls} = {sum(self.rolls)}")

    def get_dados(self, comando):
        try:
            loc_d = comando.find("d")
            if loc_d == -1:
                raise Exception("dados errados")
            if loc_d == 0:
                self.qtd = 1
                self.faces = 6
                return

            loc_s = comando.find("+")
            if loc_s == -1:
                loc_s = comando.find("-")

            self.bonus = 0
            if loc_s != -1:
                self.faces = int(comando[loc_d+1:loc_s])
                self.bonus = int(comando[loc_s:])
            else:
                self.faces = int(comando[loc_d+1:])

            self.qtd = 1
            if comando[0] != "d":
                self.qtd = int(comando[:loc_d])

        except Exception as e:
            print(f"Error: {e}" )