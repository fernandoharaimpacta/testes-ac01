import pytest
from exercicio4 import Comissao,TipoIncorreto,NumeroNegativo

def teste_caso_01_exercicio4():
    assert Comissao(75.00) == 82.50

def teste_caso_02_exercicio4():
    assert Comissao(125) == 137.50

def teste_caso_03_exercicio4():
    assert Comissao(350.87) == 385.96

def teste_caso_01_tipo_incorreto_exercicio4():
    with pytest.raises(TipoIncorreto):
        Comissao([399.20])

def teste_caso_02_tipo_incorreto_exercicio4():
    with pytest.raises(TipoIncorreto):
        Comissao('399.20')

def teste_caso_01_numero_negativo_exercicio4():
    with pytest.raises(NumeroNegativo):
        Comissao(-10.50)