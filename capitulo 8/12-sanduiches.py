def sandwich_ingr(*itens):
   print("\n Esses são os ingredientes fornecidos")
   for iten in itens:
       print(f"- {iten}") 
       
sandwich_ingr("pepperoni")
sandwich_ingr("pepperoni","salad","cheese")
sandwich_ingr("pepperoni","salad","cheese","chicken","tomatoes")

    