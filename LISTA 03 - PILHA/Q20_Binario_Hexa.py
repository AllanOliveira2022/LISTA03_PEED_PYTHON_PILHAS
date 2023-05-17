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

from Pilha_Base import Pilha

def decimal_hexa(decimal):
    pilha = Pilha()
    num = decimal
    while num > 0:
        resto = num % 16 
        num = num // 16
        if resto >=10 :
            match resto:
                case 10:
                    resto = 'A'
                case 11:
                    resto = 'B'
                case 12:
                    resto = 'C'
                case 13:
                    resto = 'D'
                case 14: 
                    resto = 'E'
                case 15:
                    resto = 'F'       
        pilha.adicionar(resto)
        print("O resto é: ",resto)
        print("Resto da divisão:",num)
    if num != 0:
        pilha.adicionar(num)
    
    hexa = []
    while not pilha.is_empty():
        pilha.top()
        hexa.append(pilha.top())
        pilha.remover()

    return hexa

binario = input("Digite o número em binário : ")
print("Número em binário: ",binario)
bin_dec = converter_decimal(binario)
hexa = decimal_hexa(bin_dec)
print("O número em Hexadecimal é: ",end="")
for i in hexa:
    print(i, end="")

