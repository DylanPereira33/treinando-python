current_users = ["luke", "Dylan", "Derick", "Matheus", "Jeniffer"]

new_users = ["Gabriel", 'Raquel', "joão", "Derick", 'Matheus']

for usuário_novo in new_users:
    if usuário_novo in current_users:
        print("você deverá fornecer um novo nome")
    else:
        print("nome de usuário disponivel")