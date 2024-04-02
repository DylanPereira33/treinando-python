car = "bmw"
print(car == 'bmw')
print(car =='mercedes')

Luke = "lucas"
print(Luke != "Dylan")
print(Luke != "lucas")

name = "Dylan"
print(name.lower() == "dylan")
print(name.lower() == 'Dylan')

number = 42
print(42 == 42)
print(42 == 33)
print(42 != 10)
print(42 != 42)
print(42 > 22)
print(42 > 48)
print(42 < 52)
print(42 < 33)
print(42 >= 18)
print(42 >= 99)
print(42 <= 55)
print(42 <= 12)

car = "bmw"
number = 10
print(car == "bmw" and number == 10 )
print(car == "bmw" and number == 42 )


car = "audi"
number = 42
print(car == "audi" or number == 10 )
print(car == "bmw" or number == 99 )

compras = ["leite", "pão", "manteiga", "carne"]
print('carne' in compras)
print("pizza" in compras)
print("feijão" not in compras)
print("leite" not in compras)