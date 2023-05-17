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

binario = input("Digite o número em binário : ")
print("Número em binário: ",binario)
bin_dec = converter_decimal(binario)
print("Número em octal: ",bin_dec)