from Pilha_Base import Pilha

def main(decimal):
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
decimal = int(input("Digite um número em decimal: "))
bin = main(decimal)
print("O número em Hexadecimal é: ")
for i in bin:
    print(i, end="")

