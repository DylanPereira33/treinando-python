def numeros_favoritos_de_todos_os_usuarios(todos_numeros_favoritos):
    for nome, numeros in todos_numeros_favoritos.items():
        numeros_favoritos_do_usuario(nome, numeros)

def numeros_favoritos_do_usuario(nome, numeros):
    if len(numeros) == 0:
        return (f"{nome} odeia números.")
    elif len(numeros) == 1:
        return (f"O numero favorito do usuário {nome} é {numeros[0]}")
    else:
        *inicio, penultimo, ultimo = numeros
        text = f"Os números favoritos do usuário {nome} são: "
        for numero in inicio:
            text += f"{numero}, "
        text += f"{penultimo} e {ultimo}"
        return text

