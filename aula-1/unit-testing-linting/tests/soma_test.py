from src.soma import soma

def test_soma_numeros_positivos():
    resultado = soma(2, 3)
    assert resultado == 5, "A soma de 2 e 3 deveria ser 5"

def test_soma_numeros_negativos():
    resultado = soma(-2, -3)
    assert resultado == -5, "A soma de -2 e -3 deveria ser -5"

def test_soma_misto_positivo_negativo():
    resultado = soma(10, -5)
    assert resultado == 5, "A soma de 10 e -5 deveria ser 5"

def test_soma_zero():
    resultado = soma(0, 0)
    assert resultado == 0, "A soma de 0 e 0 deveria ser 0"
