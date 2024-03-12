# 1- Criar uma classe User que vai ser responsável por armazenar alguns dados do usuário à sua escolha
# 2- Criar uma classe UserRepository que vai ser responsável por armazenar uma lista de usuários e também por manipular essa lista:
#   - Verificar se o usuário já existe
#   - Adicionar um usuário à lista, verificar se é uma instância de User (instanceof(obj))
#   - Fazer o login do usuário verificando a senha
#   - O que for necessário
# 3- Criar lógica pra criar um usuário à partir do input do usuário
# 4- Criar lógica pra logar com um usuário à partir do input do usuário
# 5- Salvar a senha do usuário como um hash usando a lib hashlib, e comparar os hashes ao invés da senha
# 6- Aprender como criar um à criar um json à partir da lista de usuários. Utilize list comprehension pra facilitar a criação da lista de objetos parar carregar no json 
# https://www.w3schools.com/python/python_lists_comprehension.asp
# também lembre que para ver um objeto no formato de dicionário basta chamar obj.__dict__
# 7- Aprender como ler o texto e escrever um texto num arquivo utilizando a lib Pathlib do python. Não esqueça que a extensão é .json.
# 8- Por fim, o programa deve ser capaz de salvar a lista de usuários localmente após a criação de novos usuários e deve ser capaz de popular novamente a lista de UserRepository com instancias de User.
#
# 9- Poucos pontos extras fazendo um start bonitinho e fazendo uma "UI" bonitinha
# 10- Pontos extras tratando o input corretamente.
#   - Pontos extras para usar try/except para lidar com input
# 11- Muitos pontos extras permitindo que o usuário saia e entre livremente da criação de usuário/login. Dica: Você pode criar os estados da aplicação numa pilha
# import requests
# import json

# class Pokemon:
#     def __init__(self):
#         self.base_experience = 0
# x = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
# j = json.loads(x.text)


# print(Pokemon(**j).__dict__)