filename = "guest_book.txt"

name = input("Escreva seu nome: ")
while name != "":
    print(f"Hello, {name}!")
    with open(filename,"a") as file_object:
        file_object.write(f"{name}\n")
    name = input("Escreva seu nome: ")

print("Fim")

