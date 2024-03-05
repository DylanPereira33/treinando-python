class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over")

my_dog = Dog("willy", 6)
your_dog = Dog("lucy", 3)

print(f"my dog name is {my_dog.name}.")
print(f"my dog is {my_dog.age} years old.")
my_dog.sit()

print(f"my dog name is {your_dog.name}.")
print(f"my dog is {your_dog.age} years old.")
your_dog.sit()
