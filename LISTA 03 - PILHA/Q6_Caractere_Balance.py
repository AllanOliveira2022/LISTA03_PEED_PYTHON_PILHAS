from Pilha_Base import Pilha

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
           
expressao = input("Digite o conjunto de caracteres '(,),{,},[,]': ")
if esta_balanceada(expressao):
    print("Os caracteres estão BALANCEADOS.")
else:
    print("os caracteres estão DESBALANCEADOS !")