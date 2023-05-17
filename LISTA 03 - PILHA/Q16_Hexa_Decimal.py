from Pilha_Base import Pilha

def converter_decimal(hexa):
    pilha = Pilha()
#Empilhando os valores

    for digito in hexa:
        pilha.adicionar(digito)
    
    #desempilhando e transformando
    exp = 0
    decimal =0
    while not pilha.is_empty(): 
        num = pilha.remover()
        if num.isdigit():
            decimal+= int(num) * (16 ** exp)
        else:    
            if num =="A":
                decimal+= 10 * (16 ** exp)
            elif num =="B":
                decimal+= 11 * (16 ** exp)
            elif num == "C":
                decimal+= 12 * (16 ** exp)  
            elif num == "D":
                decimal+= 13 * (16 ** exp) 
            elif num == "E":
                decimal+= 14 * (16 ** exp) 
            elif num == "F":
                decimal+= 15 * (16 ** exp)                                                           
        exp += 1        
    return decimal

hexa= input("Digite o número em Hexadecimal com letras MAIÚSCULAS: ")
print("Número em Hexadecimal: ",hexa)
hexa_dec = converter_decimal(hexa)
print("Número em decimal: ",hexa_dec)