from Pilha_Base import Pilha

def converter_para_notacao_polonesa(expressao):
    pilha = Pilha()
    notacao_polonesa = []
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}

    for caracter in expressao:
        if caracter.isnumeric():
            notacao_polonesa.append(caracter)
        elif caracter in '+-*/':
            while not pilha.is_empty() and pilha.top() in '+-*/' and precedencia[caracter] <= precedencia[pilha.top()]:
                notacao_polonesa.append(pilha.remover())
            pilha.adicionar(caracter)
        elif caracter == '(':
            pilha.adicionar(caracter)
        elif caracter == ')':
            while not pilha.is_empty() and pilha.top() != '(':
                notacao_polonesa.append(pilha.remover())
            pilha.remover()

    while not pilha.is_empty():
        notacao_polonesa.append(pilha.remover())

    return ''.join(notacao_polonesa)


# Exemplo de uso
expressao = input("Digite uma expressão matematica: ")
notacao_polonesa = converter_para_notacao_polonesa(expressao)
print("Notação polonesa reversa:", notacao_polonesa)