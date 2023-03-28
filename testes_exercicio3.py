import pytest
from exercicio3 import DescontoValor,TipoIncorreto,NumeroNegativo,ValorZerado,Prejuizo

def teste_caso_01_exercicio3():
    assert DescontoValor(500.00, 50.00) == 450.00

def teste_caso_02_exercicio3():
    assert DescontoValor(10500.00, 500.00) == 10000.00

def teste_caso_03_exercicio3():
    assert DescontoValor(90.00, 0.80) == 89.20

def teste_caso_01_tipo_incorreto_exercicio3():
    with pytest.raises(TipoIncorreto):
        DescontoValor([500.00], 50.00)

def teste_caso_02_tipo_incorreto_exercicio3():
    with pytest.raises(TipoIncorreto):
        DescontoValor('500.00', 50.00)

def teste_caso_03_tipo_incorreto_exercicio3():
    with pytest.raises(TipoIncorreto):
        DescontoValor(500.00, '50.00')

def teste_caso_01_valor_zerado_exercicio3():
    with pytest.raises(ValorZerado):
        DescontoValor(0, 50.00)

def teste_caso_01_prejuizo_exercicio3():
    with pytest.raises(Prejuizo):
        DescontoValor(50.00, 100.00)

def teste_caso_01_numero_negativo_exercicio3():
    with pytest.raises(NumeroNegativo):
        DescontoValor(-50.00, 100)

def teste_caso_02_numero_negativo_exercicio3():
    with pytest.raises(NumeroNegativo):
        DescontoValor(50.00, -100.00)