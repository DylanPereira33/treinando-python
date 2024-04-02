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

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges 
        
    def show_privileges(self):
        print("Privileges")
        for privilege in self.privileges:
            print(privilege)
            
           
class Admin(User):
    def __init__(self,first_name,last_name,age,location,privileges):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.privileges = Privileges(privileges)
    
   
admin_1 = Admin('Gabriel',"Nascimento",34,"Canadá", ["can add post", "can delete post", "can ban user"])
admin_1.privileges.show_privileges()