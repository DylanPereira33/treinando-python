filename = "guest_book.txt"

while True:
    name = input("Qual é o seu nome?")
    if name != "":
        print(f"Hello, {name}!")
        with open(filename,"a") as file_object:
            file_object.write(f"{name}\n")
    else:
        break
print("Fim")
            
        