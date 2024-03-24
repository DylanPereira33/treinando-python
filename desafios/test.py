from random import randint

print("Role um dado")

class Roll:
    def __init__(self,faces,qtd=1,bonus=0):
        self.faces = faces
        self.qtd = qtd
        self.bonus = bonus
        self.rolls = []
        
    def roll(self):
        for _ in range(self.qtd):
            self.rolls.append(int(1, self.faces))
            
            if self.bonus < 0:
                print(f"{self.rolls}{self.bonus} = {sum(self.rolls) + self.bonus}")
            elif self.bonus > 0:
                print(f"{self.rolls} + {self.bonus} = {sum(self.rolls) + self.bonus}")
            else:
                print(f"{self.rolls} = {sum(self.rolls)}")
            
def input(comando):
    loc_d = comando.find("d")
    if loc_d == -1:
        raise Exception("formato incorreto")
        
        bonus = 0
        loc_s = comando.find("+")
        if loc_s == -1:
            loc_s = comando.find("-")
        
        if loc_s != -1:
            faces = int(comando[loc_d+1:loc_s])
            bonus = int(comando[loc_s:])
        else:
            faces = int(comando[loc_d+1:])
            
        qtd = 1
        if comando[0] != "d":
            qtd = int(comando[:loc_d])

            return (faces,qtd,bonus)
           
while True:
    (faces,qtd,bonus) = (0,0,0)
    comando = input("Roll:")
    if comando == "":
        break
    
    (faces,qtd,bonus) = input(comando)
    rolagem = Roll(faces,qtd,bonus)
    rolagem.roll()
    
    
      
print("fim de jogo")    