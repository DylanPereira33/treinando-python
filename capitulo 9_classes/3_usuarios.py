class User:
    def __init__(self,first_name,last_name,age,location):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
    
    def describe_user(self):
        print(f"Meu nome é {self.first_name} {self.last_name}")
        print(f"Tenho {self.age} e moro no {self.location}")
    
    def greet_user(self):
        print(f"Olá {self.first_name} {self.last_name}")

my_user = User('Gabriel',"Nascimento",34,"Canadá")
your_user = User("Carol","Lima",28, "Brasil")

my_user.describe_user()
my_user.greet_user()
print("--------")
your_user.describe_user()
your_user.greet_user()