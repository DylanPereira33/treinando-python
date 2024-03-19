from random import choice

lista = [1,2,3,4,5,6,7,8,9,0,"a","b","c","d","e"]

my_ticket = choice(lista)

for i in range(0,len(lista)):
    print(choice(lista))
    if lista[i] == my_ticket:
        print(f"foram necessários {i+1} tentativas para sortear o seu valor {lista[i]}")
        break
    

