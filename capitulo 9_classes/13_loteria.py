from random import choice

lista = [1,2,3,4,5,6,7,8,9,0,"a","b","c","d","e"]

for roll in range(0,4):
    print(choice(lista))

print(f"Qualquer bilhete que tiver esses valores ganha um prêmio!")