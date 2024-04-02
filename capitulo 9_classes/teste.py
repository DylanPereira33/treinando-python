# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def sit(self):
#         print(f"{self.name} is now sitting")

#     def roll_over(self):
#         print(f"{self.name} rolled over")

# my_dog = Dog("willy", 6)
# your_dog = Dog("lucy", 3)

# print(f"my dog name is {my_dog.name}.")
# print(f"my dog is {my_dog.age} years old.")
# my_dog.sit()

# print(f"my dog name is {your_dog.name}.")
# print(f"my dog is {your_dog.age} years old.")
# your_dog.sit()

class Car():
    def __init__(self,make,model,year):
        self.make = make 
        self.model = model 
        self.year = year
    
    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()
    
my_new_car = Car("audi","a4",2016)
print(my_new_car.get_descriptive_name())