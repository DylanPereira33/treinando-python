class Restaurant:
    def __init__(self,name,type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f"{self.name} é o nome do nosso restaurante")
        print(f"Comida {self.type} é o tipo de nosso restaurante ")

    def open_restaurant(self):
        print(f"O {self.name} esta aberto!")

my_restaurant = Restaurant("Outback", "Australiana")
your_restaurant = Restaurant("habibs", "Árabe")
praça_restaurant = Restaurant("Sushi da Praça", "Japônesa")
my_restaurant.describe_restaurant()
praça_restaurant.describe_restaurant()
your_restaurant.describe_restaurant()