import json
filename = "username.json"
def get_stored_username():

    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
 username = input("What is your name? ") 
 filename = 'username.json'
 with open(filename, 'w') as f_obj:
     json.dump(username, f_obj) 
     return username
 
def greet_user(): 
    username = get_stored_username() 
    if username: 
        answer = input(f"Hello, is this the correct username:{username} (yes or no)?")
        if answer.lower() == "yes":
            print(f"Welcome back,{username} !") 
        else:
            username = get_new_username()
            print("We'll remember you")
    else: 
        username = get_new_username() 
        print(f"We'll remember you when you come back, {username} !")
        
greet_user()