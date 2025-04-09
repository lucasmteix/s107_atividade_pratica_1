def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

def potencia(a, b):
    return a ** b

def fatorial(n):
    if n < 0:
        return "Erro: fatorial de número negativo"
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def raiz_quadrada(n):
    if n < 0:
        return "Erro: raiz de número negativo"
    return n ** 0.5