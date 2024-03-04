person_0 = {'first_name':'Derick','last_name':'Pereira','age':14,'city':'Rio de Janeiro'}
person_1 = {'first_name':'Dylan','last_name':'Pereira','age':18,'city':'Rio de Janeiro'}
person_2 = {'first_name':'Luke','last_name':'Dias','age':24,'city':'Rio de Janeiro'}

people = (person_0,person_1,person_2)

for person in people:
    for k,v in person.items():
        print(f"{k} : {v}")
    print("\n")