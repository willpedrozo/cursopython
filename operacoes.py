# funcao para somar dois numeros
def somar(a, b):
    return a + b #retorna a soma de a e b

def subtrair(a, b):
    return a - b #retorna a subtração de a e b

def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por 0")
        #levanta o erro se b for 0
    return a / b