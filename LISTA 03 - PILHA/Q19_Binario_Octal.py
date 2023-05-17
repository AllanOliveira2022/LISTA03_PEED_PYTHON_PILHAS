from Pilha_Base import Pilha

def converter_decimal(binario):
    pilha = Pilha()
    tam =0
#Empilhando os valores
    for digito in binario:
        valor= int(digito)
        pilha.adicionar(valor)
        tam += 1
    
    #desempilhando e transformando
    decimal =0
    for cont in range(0,tam):
        valor = pilha.remover()
        if valor == 1:
            decimal+= (valor * 2) ** cont

    return decimal
def converter_octal(decimal):
    pilha = Pilha()
    num = decimal
    while num > 0:
        resto = num % 8 
        num = num // 8
        pilha.adicionar(resto)
        print("O resto é: ",resto)
        print("Resto da divisão:",num)
    if num != 0:
        pilha.adicionar(num)
    
    octal = []
    while not pilha.is_empty():
        pilha.top()
        octal.append(pilha.top())
        pilha.remover()

    return octal
binario = input("Digite o número em binário : ")
print("Número em binário: ",binario)
decimal= converter_decimal(binario)
octal = converter_octal(decimal)
print("Número em octal: ",octal)