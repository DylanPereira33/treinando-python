prompt = "\n Quais ingredientes você quer colocar em sua pizza?"
prompt += "\n Ao finalizar sua pizza, digite 'quit'"

pizza = True
while pizza:
    pedido = input(prompt)
    if pedido == 'quit':
        pizza = False
    else:
        print(f"Adicionando {pedido}")
    
