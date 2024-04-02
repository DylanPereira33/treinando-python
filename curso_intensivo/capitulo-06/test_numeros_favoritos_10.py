from numeros_favoritos_10 import numeros_favoritos_do_usuario

def test_no_numbers():
    # Arrange 
    name = "test"
    numbers = []

    # Act

    resultado = numeros_favoritos_do_usuario(name, numbers)
    # Assert
    assert resultado == f"{name} odeia números."

def test_one_numbers():
    # Arrange
    name = "test"
    numbers = [42]

    # Act
    resultado = numeros_favoritos_do_usuario(name, numbers)

    # Assert
    assert resultado == f"O numero favorito do usuário {name} é {numbers[0]}"

def test_many_numbers():
    # Arrange
    name = "test"
    numbers = [42, 13, 69, 30]

    # Act
    resultado = numeros_favoritos_do_usuario(name,numbers)

    # Assert
    assert resultado == f"Os números favoritos do usuário {name} são: {numbers[0]}, {numbers[1]}, {numbers[2]} e {numbers[3]}"


def test_doble_numbers():
    # Arrange
    name = "test"
    numbers = [42,33]

    # Act
    result = numeros_favoritos_do_usuario(name,numbers)

    # Assert 
    assert result == f"Os números favoritos do usuário {name} são: {numbers[0]} e {numbers[1]}"