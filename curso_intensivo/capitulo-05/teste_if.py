# convidados =   ['luke', 
#                 'jen', 
#                 'tom',
#                 'raquel',
#                 'derek', 
#                 'paula',
#                 'chico']

# numeros = [8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

# number = 10
# if number > 5:
#     print('que número grande!')


# cars = ["audi", "bmw", "subaru", "toyota"]

# for car in cars:
#     if car == "bmw":
#         print(car.upper())
#     else:
#         print(car.title())

# car = 'Audi'
# print(car.lower() == 'audi')

# print(car)

# requested_toppings = ['mushrooms', 'onions', 'pineapple']

# print('mushrooms' in requested_toppings)
# print('cereja' in requested_toppings)

sabores_disponiveis = ["pepperoni", 'carne', "camarão"]
sabores_pedidos = ["camarão",'queijo']
pizzas_indisponiveis = []

for sabor_pedido in sabores_pedidos:
    if sabor_pedido not in sabores_disponiveis:
        pizzas_indisponiveis.append(sabor_pedido)

if pizzas_indisponiveis:
    print(f"sabores indisponveis: {pizzas_indisponiveis}")
else:
    print("fazendo sua pizza!")


        