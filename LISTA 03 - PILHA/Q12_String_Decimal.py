from Pilha_Base import Pilha

def converter_para_decimal(string):
    pilha = Pilha()
    for digito in string:
        pilha.adicionar(int(digito))

    resultado = 0
    posicao = 0

    while not pilha.is_empty():
        resultado += pilha.remover() * 10**posicao
        posicao += 1

    return resultado

string = input("Digite um número: ")
print("tipo antes da conversão",type(string))
numero_decimal = converter_para_decimal(string)
print("Número convertido para inteiro: ",numero_decimal)
print("Tipo depois da conversão",type(numero_decimal))