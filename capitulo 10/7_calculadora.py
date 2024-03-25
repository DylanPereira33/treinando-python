print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("first_number:")
    if first_number == "q":
         break
    second_number = input("second_number:")
    if second_number == "q":
         break
    try: 
        asnwer = int(first_number) + int(second_number) 
    except ValueError:
        print(" Não apresenta números")
    else:
        print(asnwer)  