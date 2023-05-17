from Pilha_Base import Pilha   
def infixa_para_posfixa(expressao):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operadores = Pilha()
    posfixa = []
    numeros = '0123456789'
    for caracter in expressao:
        if caracter in numeros:
            posfixa.append(caracter)
        elif caracter in precedencia:
            while not operadores.is_empty()  \
                and operadores.top() != '(' \
                and precedencia[caracter] <= precedencia[operadores.top()]:
                posfixa.append(operadores.remover())
            operadores.adicionar(caracter)
    while not operadores.is_empty():
        posfixa.append(operadores.remover())
    return ''.join(posfixa)

def calcular(expressao):
    pilha = Pilha()
    for c in expressao:
        if c.isdigit():
            pilha.adicionar(int(c))
        elif c in "+-*/":
            b = pilha.remover()
            a = pilha.remover()
            if c == "+":
                pilha.adicionar(a + b)
            elif c == "-":
                pilha.adicionar(a - b)
            elif c == "*":
                pilha.adicionar(a * b)
            elif c == "/":
                pilha.adicionar(a / b)
    return pilha.remover()

s = input("Digite a expressão infixa: ")

posfixa = infixa_para_posfixa(s)

resultado = calcular(posfixa)

print("\nResultado: ",resultado)


