sandwich_orders = ["pastrami","hamburguer","pastrami","queijo-quente","pastrami","pão com presunto"]
finish_sandwiches = []

print("estamos sem pastrami!")

while "pastrami" in sandwich_orders:
   sandwich_orders.remove("pastrami")

print(sandwich_orders)

while sandwich_orders:
        sandwich = sandwich_orders.pop()

        print(f"seu {sandwich} está sendo preparado!")
        finish_sandwiches.append(sandwich)

print("\nsandwiches prontos")
for sandwich in finish_sandwiches:
        print(sandwich)