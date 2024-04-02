from test import Roll

def test_roll_eh_criado_sem_popular_dados():
    roll = Roll()

    # Act
    roll.get_dados("d")

    # Assert
    assert roll.qtd == 1
    assert roll.faces == 0
    assert roll.bonus == 0


def test_roll_eh_criado_sem_popular_dados_negatives():
    roll = Roll()
    roll.get_dados("1d6-10")
    assert roll.qtd == 1
    assert roll.faces == 6
    assert roll.bonus == -10


def test_roll_eh_criado_sem_popular_dados_positivos():
    test_cases = [("1d6+10", 1, 6, 10), ("20d66+12", 20, 66, 12)]
    for test in test_cases:
        roll = Roll()
        roll.get_dados(test[0])
        assert roll.qtd == test[1]
        assert roll.faces == test[2]
        assert roll.bonus == test[3]
