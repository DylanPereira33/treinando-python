first_number = input("first_number:")
second_number = input("second_number:")

try:
     asnwer = int(first_number) + int(second_number)
     print(asnwer)
except ValueError:
    print(" Não apresenta números")
