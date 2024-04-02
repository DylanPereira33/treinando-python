filename = "cats.txt"
filename2 = "dogs.txt"

def count_cats(filename):
    try: 
        with open(filename) as cats:
            count = cats.read()
            
    except FileNotFoundError:
        pass
    else:
        print(count)
        
def count_dogs(filename2):
    try: 
        with open(filename2) as dogs:
            count = dogs.read()
            
    except FileNotFoundError:
        pass
    else:
        print(count)
 
count_cats(filename)
print("------------")      
count_dogs(filename2)
 