from Pilha_Base import Pilha

def converter_decimal(octal):
    pilha = Pilha()
    tam =0
#Empilhando os valores
    for digito in octal:
        valor= int(digito)
        pilha.adicionar(valor)
        tam += 1
    
    #desempilhando e transformando
    decimal =0
    for cont in range(0,tam):
        valor = pilha.remover()
        decimal+= valor * (8 ** cont)

    return decimal

octal = input("Digite o número em Octal : ")
print("Número em Octal: ",octal)
octal_dec = converter_decimal(octal)
print("Número em decimal: ",octal_dec)