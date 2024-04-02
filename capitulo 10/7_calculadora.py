print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

first_number = input("first number: ")
while first_number != "q":
    second_number = input("second number: ")
    try:
        answer = int(first_number) + int(second_number) 
    except ValueError:
        print(" Não apresenta números")
    else:
        print(answer)
    first_number = input("first number: ")
