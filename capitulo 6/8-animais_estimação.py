cachorro = {'vira_lata':'Raquel','Poodle':'Ana'}
gato = {'persa':'Chico','Siamês':'Carla'}

pets = [cachorro, gato]

for pet in pets:
    for k,v in pet.items():
        print(f"{k} : {v}")
    print("\n")
