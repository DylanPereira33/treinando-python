sandwich_orders = ["hamburguer","queijo-quente","pão com presunto"]
finish_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"seu {sandwich} está sendo preparado!")
    finish_sandwiches.append(sandwich)

print("\nsandwiches prontos")
for sandwich in finish_sandwiches:
    print(sandwich)
