# Desafio 
## Desafio Stone
1. Criar uma API usando DJango e Python 3 responsável por administrar contas bancárias.
2. Essa API precisa ter pelo menos 3 endpoints relacionados ao CRUD do usuário:
  1. Criar uma conta no banco.
  2. Atualizar dados da conta.
  3. Ler os dados de uma conta.
  4. Deletar uma conta.
3. Além disso, essa API precisa de mais 3 endpoints relacionados ao extrato da conta:
  1. Depositar uma quantidade de dinheiro.
  2. Sacar uma quantidade de dinheiro.
  3. Transferir dinheiro entre conta bancárias.
4. Pra armazenar isso você precisa utilizar um banco de dados, podendo ser o LiteSQL ou o PostgresSQL.

5. Você precisa armazenar, além dos dados do usuário, um histórico de todas as transações feitas por uma conta. (E se uma conta receber uma transação, isso deve ser armazenado também)
6. A API precisa de um endpoint para fazer o login, onde ela irá gerar um token JWT para ser usado nas outras requisições (basicamente um sistema de autenticação)

7. A API precisa ter todos as funções públicas devidamente testadas, utilizando testes unitários.
8. A API precisa retornar o status correto em cada response.
9. Configurar o Swagger para facilitar testar os endpoints.

## Desafio Maino
1. Criar uma API usando DJango, Python 3 e a PokeAPI responsável por administrar uma conta de um jogador de Pokémon.
2. Essa API precisa ser capaz de realizar as operações CRUD e autenticar um usuário.
3. É preciso ser capaz de visualizar uma lista de pokemons por geração (se tiver na PokeAPI)
4. É preciso ser capaz de fazer um CRUD de Pokémon em relação à um time:
  1. Tirar um Pokémon
  2. Ler um time.
  3. Trocar um Pokémon por outro.
  4. Adicionar um Pokémon ao time.
5. Cada conta pode ter 10 times. Cada time, pode ter de 1-6 Pokémons, porém não podem existir times vazios.
6. Deve ser possível adicionar uma conta como amiga de outra. (relação many-to-many)
7. Se duas contas tiverem amizade, deve ser possível ver os times da outra conta.

## Desafio Hurb v0
1. Criar um projeto onde o usuário consegue, pelo terminal fazer uma pesquisa de câmbio. ex:
```bash
python3 cmd-cambio usd brl 1000
```
2. Ele deve ser capaz de guardar esse valor e só atualizar quando novos dados estiverem disponíveis.
  - Escolher um API que faça câmbio e explicar pq escolheu ela.
  - Entender de quanto em quanto tempo essa API é atualizada e só carregar novos valores para as moedas quando tiver dados novos.
  - Não fazer a requisição direta do câmbio, mas pegar os dados em dólar de todas as moedas e calcular a conversão entre elas.
  - Mesmo sem a aplicação estar rodando, só deve chamar a API de câmbio se houver atualização. (Guardar os dados das moedas e os dados de quando foi a última requisição e os dados de quanto em quanto tempo há atualização)
3. Não precisa usar um banco de dados, mas ganha pontos por utilizar o redis.
