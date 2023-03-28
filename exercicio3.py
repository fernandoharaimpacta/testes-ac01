class TipoIncorreto(Exception):
    pass

class NumeroNegativo(Exception):
    pass

class ValorZerado(Exception):
    pass

class Prejuizo(Exception):
    pass

def DescontoValor(valor, desconto):
    if type(valor) != int and type(valor) != float:
        raise TipoIncorreto
    
    if type(desconto) != int and type(desconto) != float:
        raise TipoIncorreto
    
    if valor == 0:
        raise ValorZerado

    if valor < 0 or desconto < 0:
        raise NumeroNegativo
    
    value = round(valor - desconto, 2)
    if value < 0:
        raise Prejuizo
    
    return value