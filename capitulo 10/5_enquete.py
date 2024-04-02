filename = "enquete.txt"

comando = input("Por que você gosta de programação? ")
while comando != "":
    with open(filename, "a") as file_object:
        file_object.write(f"{comando}\n")
    comando = input("Por que você gosta de programação? ")

print("Fim")

