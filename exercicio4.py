class TipoIncorreto(Exception):
    pass

class NumeroNegativo(Exception):
    pass

def Comissao(valor):
    if type(valor) != float and type(valor) != int:
        raise TipoIncorreto
    
    if valor < 0:
        raise NumeroNegativo
    
    gorjeta = valor * (10 / 100)
    return round(valor + gorjeta, 2)

if __name__ == "__main__":
    print(Comissao(75.00))