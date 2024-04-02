class Restaurant:
    def __init__(self,name,type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f"{self.name} é o nome do nosso restaurante")
        print(f"Comida {self.type} é o tipo de nosso restaurante ")

    def open_restaurant(self):
        print(f"O {self.name} esta aberto!")
        
class IcecreamStand(Restaurant):
    
    def __init__(self, name, type, flavors):
        super().__init__(name, type)
        
        self.flavors = flavors
        
    def choice_flavors(self):
        print(f"The flavors are:")
        for flavor in self.flavors:
            print(flavor)
            
Icecream = IcecreamStand("Eskimó", "Ice cream", ["chocolate", "Banana", "strawberry"])
Icecream.choice_flavors()
