class TipoIncorreto(Exception):
    pass

class NumeroNegativo(Exception):
    pass

class ValorZerado(Exception):
    pass

def CalculaDescontoLoja(valor):
    if type(valor) != float and type(valor) != int:
        raise TipoIncorreto

    if valor < 0:
        raise NumeroNegativo

    if valor == 0:
        raise ValorZerado

    desc = valor * (9 / 100)
    return round(valor - desc, 2)

if __name__ == '__main__':
    print(CalculaDescontoLoja(100))