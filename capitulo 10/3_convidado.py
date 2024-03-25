filename = "guest.txt"

comando = input("Qual é o seu nome?")

with open(filename,"a") as file_object:
    file_object.write(f"{comando}\n")
    