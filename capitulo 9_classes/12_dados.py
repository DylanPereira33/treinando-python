class Die:
    def __init__(self,sides):
        self.sides = sides

    def roll_die(self):
        from random import randint
        print(randint(1,self.sides))

d6 = Die(6)
d10 = Die(10)
d20 = Die(20)

for roll in range(0,10):
    d6.roll_die()
    d10.roll_die()  
    d20.roll_die()         
