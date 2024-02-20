mapa = """------------
|.#........|
|..###..#..|
|.....#..#.|
|.####.#P#.|
|.......#..|
|#.####...#|
|#.....#.##|
|.###...#..|
|.#...#.#.#|
|c..#.....#|
------------"""

# Transformar o mapa em uma lista de strings
mapa = mapa.split('\n')

# Localização inicial do personagem 'c'
posicao_c = 0
posicao_p = 0

for i, linha in enumerate(mapa):
    if 'c' in linha:
        posicao_c = (i, linha.index('c'))
    if 'P' in linha:
        posicao_p = (i, linha.index('P'))

# Função para imprimir o mapa
def imprimir_mapa():
    for linha in mapa:
        print(''.join(linha))

# Loop para mover o personagem até o ponto final 'P'
while  posicao_c != posicao_p:
    imprimir_mapa()
    comando = input("Digite um comando (w, s, a, d): ")
    
    # Atualizar a posição do personagem de acordo com o comando
    if comando == 'w':  # mover para cima
        nova_posicao = (posicao_c[0] - 1, posicao_c[1])
    elif comando == 's':  # mover para baixo
        nova_posicao = (posicao_c[0] + 1, posicao_c[1])
    elif comando == 'a':  # mover para esquerda
        nova_posicao = (posicao_c[0], posicao_c[1] - 1)
    elif comando == 'd':  # mover para direita
        nova_posicao = (posicao_c[0], posicao_c[1] + 1)
    else:
        print("Comando inválido. Use w, s, a ou d.")
        
    # Verificar se a nova posição é válida (não ultrapassa os limites do mapa e não é um obstáculo)
    if mapa[nova_posicao[0]][nova_posicao[1]] != '#':
      
    # Atualizar o mapa com a nova posição do personagem 'c'
        mapa[posicao_c[0]] = mapa[posicao_c[0]].replace('c', '.')  # Substitui a posição anterior por um espaço vazio
        mapa[nova_posicao[0]] = mapa[nova_posicao[0]][:nova_posicao[1]] + 'c' + mapa[nova_posicao[0]][nova_posicao[1] + 1:]
        posicao_c = nova_posicao

    else:
        print("Movimento inválido. Tente novamente.")

print("Parabéns! Você chegou ao ponto final 'P'.")









