import pytest
from exercicio1 import CalcularSalarioLiquido,NumeroNegativo,TipoIncorreto

def teste_caso_01_exercicio1():
    assert CalcularSalarioLiquido(6.25, 160, 1.3) == 987.00

def teste_caso_02_exercicio1():
    assert CalcularSalarioLiquido(20.5, 240, 1.7) == 4836.36

def teste_caso_03_exercicio1():
    assert CalcularSalarioLiquido(13.9, 200, 6.48) == 2599.86

def teste_caso_string_01_exercicio1():
    with pytest.raises(TipoIncorreto):
        CalcularSalarioLiquido('6.25', 160,1.3)

def teste_caso_lista_exercicio1():
    with pytest.raises(TipoIncorreto):
        CalcularSalarioLiquido(6.25, [160], 1.3)

def teste_caso_string_e_lista_exercicio1():
    with pytest.raises(TipoIncorreto):
        CalcularSalarioLiquido([123142], '160', '1.3')

def teste_caso_negativo_01_exercicio1():
    with pytest.raises(NumeroNegativo):
        CalcularSalarioLiquido(-1, 160, 1.3)

def teste_caso_negativo_02_exercicio1():
    with pytest.raises(NumeroNegativo):
        CalcularSalarioLiquido(6.25, 160, -1.3)

def teste_caso_negativo_03_exercicio1():
    with pytest.raises(NumeroNegativo):
        CalcularSalarioLiquido(6.25, -160, 1.3)