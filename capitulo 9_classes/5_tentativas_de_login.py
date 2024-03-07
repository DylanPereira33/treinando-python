class User:
    def __init__(self,first_name,last_name,age,location):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"Meu nome é {self.first_name} {self.last_name}")
        print(f"Tenho {self.age} e moro no {self.location}")
    
    def greet_user(self):
        print(f"Olá {self.first_name} {self.last_name}")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0

my_user = User('Gabriel',"Nascimento",34,"Canadá")
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
print(my_user.login_attempts)
my_user.reset_login_attempts()
print(my_user.login_attempts)