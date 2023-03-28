class NumeroNegativo(Exception):
    pass
    
class TipoIncorreto(Exception):
    pass

def CalcularSalarioLiquido(valorHoraAula, numeroAulas, percDescontoINSS):
    if type(valorHoraAula) != int and type(valorHoraAula) != float:
        raise TipoIncorreto
    
    if type(numeroAulas) != int:
        raise TipoIncorreto

    if type(percDescontoINSS) != int and type(percDescontoINSS) != float:
         raise TipoIncorreto
    
    if valorHoraAula < 0 or numeroAulas < 0 or percDescontoINSS < 0:
        raise NumeroNegativo
    
    salarioBruto = valorHoraAula * numeroAulas
    descontoINSS = salarioBruto * (percDescontoINSS / 100)
    salarioLiquido = salarioBruto - descontoINSS
    return round(salarioLiquido, 2)

if __name__ == "__main__":
    CalcularSalarioLiquido(6.25, 160, 1.3)