import pytest
from exercicio2 import CalculaDescontoLoja,TipoIncorreto,NumeroNegativo,ValorZerado

def teste_caso_01_exercicio2():
    assert CalculaDescontoLoja(100) == 91.00

def teste_caso_02_exercicio2():
    assert CalculaDescontoLoja(1500) == 1365.00

def teste_caso_03_exercicio2():
    assert CalculaDescontoLoja(60000) == 54600.00

def teste_caso_01_tipo_incorreto_exercicio2():
    with pytest.raises(TipoIncorreto):
        CalculaDescontoLoja('100')

def teste_caso_02_tipo_incorreto_exercicio2():
    with pytest.raises(TipoIncorreto):
        CalculaDescontoLoja([100])

def teste_caso_03_tipo_incorreto_exercicio2():
    with pytest.raises(TipoIncorreto):
        CalculaDescontoLoja({ "valor": 100 })

def test_caso_01_valor_negativo_exercicio2():
    with pytest.raises(NumeroNegativo):
        CalculaDescontoLoja(-100)

def test_caso_01_valor_zerado_exercicio2():
    with pytest.raises(ValorZerado):
        CalculaDescontoLoja(0)