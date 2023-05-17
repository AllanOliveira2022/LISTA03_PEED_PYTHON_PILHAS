from Pilha_Base import Pilha    
def infixa_para_posfixa(expressao):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operadores = Pilha()
    posfixa = []
    numeros = '0123456789'
    for caracter in expressao:
        if caracter in numeros:
            posfixa.append(caracter)
        elif caracter == '(':
            operadores.adicionar(caracter)
        elif caracter == ')':
            while operadores.top() != '(':
                posfixa.append(operadores.remover())
            operadores.remover()
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

def esta_balanceada(expressao):
    pilha = Pilha()
    for char in expressao:
        if char in '({[':
            pilha.adicionar(char)
        elif char in ')}]':
            if pilha.is_empty():
                return False
            topo = pilha.remover()
            if not correspondente(topo, char):
                return False
    return pilha.is_empty()

def correspondente(abertura, fechamento):
    return abertura == '(' and fechamento == ')' or \
           abertura == '{' and fechamento == '}' or \
           abertura == '[' and fechamento == ']'


s = input("Digite a expressão: ")
balanco = esta_balanceada(s)
posfixa = infixa_para_posfixa(s)

r = calcular(posfixa)
if esta_balanceada(s):
    print("A função é válida !")
    print("Resultado: ",r)
else:
    print("A equação não é válida !")
