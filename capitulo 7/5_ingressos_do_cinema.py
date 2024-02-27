prompt = "\n Qual é a sua idade?"
prompt += "\n Ao finalizar o pagamento,digite 'quit'"


ingresso = True
while ingresso:
    idade = input(prompt)
    

    if idade == 'quit':
        break
    else:
        idade = int(idade)

    if idade < 3:
        preço = "gratuito"
    if idade < 12:
        preço = 'US$10'
    else:
        preço = 'US$15'
    print(f'Seu ingresso custa {preço}')

        