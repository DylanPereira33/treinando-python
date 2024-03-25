filename = "enquete.txt"

while True:
    comando = input("Por que você gosta de programação?")
    if comando == "":
        break
    else:
        with open(filename, "a") as file_object:
            file_object.write(f"{comando}\n")
     
print("FIM")