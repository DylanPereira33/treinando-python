class Restaurant:
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"{self.name} é o nome do nosso restaurante")
        print(f"Comida {self.type} é o tipo de nosso restaurante ")

    def open_restaurant(self):
        print(f"O {self.name} esta aberto!")
    
    def set_number_served(self,served):
        self.number_served = served
        
    def increment_number_served(self,increment):
        self.number_served += increment
        

restaurant = Restaurant("Outback", "Australiana")
print(restaurant.number_served)

restaurant.number_served = 50
print(restaurant.number_served)

restaurant.set_number_served(100)
print(restaurant.number_served)

restaurant.increment_number_served(200)
print(restaurant.number_served)