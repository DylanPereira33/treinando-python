import time
import os

mapa = """------------------
|.#........#..#..|
|..###..#.....#..|
|.....#..##.....#|
|.####.#P#.###...|
|.......#...#...#|
|#.####...#.#..#.|
|#.....#.##.#..#.|
|.###...#......#.|
|.....#.###.#.#..|
|.#.#.#...#.#....|
|.#.#.#...###.##.|
|.#...#.#.#.#....|
|c..#.....#....##|
------------------"""

# Transformar o mapa em uma lista de strings
# Localização inicial do personagem 'c'
posicao_c = mapa.index('c')
posicao_p = mapa.index('P')

def desenhaMapa():
    os.system('clear')
    print(mapa)

colunas = len(mapa.split("\n")[0])+1
desenhaMapa()
inputs = ['w', 'a', 's', 'd']
startTime = 0
while  posicao_c != posicao_p:
    comandos = input("Digite um comando (w, s, a, d): ")
    hasError = False
    for comando in comandos:
        if comando not in inputs:
            desenhaMapa()
            print("Algum comando inválido. Use w, s, a ou d.")
            hasError = True
            break

    if hasError:
        continue
    for comando in comandos:
        # Atualizar a posição do personagem de acordo com o comando
        if comando[0] == 'w':  # mover para cima
            nova_posicao = posicao_c - colunas
        elif comando[0] == 's':  # mover para baixo
            nova_posicao = posicao_c + colunas
        elif comando[0] == 'a':  # mover para esquerda
            nova_posicao = posicao_c - 1
        elif comando[0] == 'd':  # mover para direita
            nova_posicao = posicao_c + 1

        if startTime == 0:
            startTime = time.perf_counter()

        place = mapa[nova_posicao]
        # Verificar se a nova posição é válida (não ultrapassa os limites do mapa e não é um obstáculo)
        if place == '#'or place == "|"or place == "-":
            desenhaMapa()
            print("Movimento inválido. Tente novamente.")
            break

        # Atualizar o mapa com a nova posição do personagem 'c'
        mapa = mapa.replace('c', '.')  # Substitui a posição anterior por um espaço vazio
        mapa = mapa[:nova_posicao] + 'c' + mapa[nova_posicao + 1:]
        posicao_c = nova_posicao
        desenhaMapa()

endTime = time.perf_counter()
elapsedTime = endTime - startTime
print(f"Parabéns! Você chegou ao objetivo. {elapsedTime:.2f}s")









