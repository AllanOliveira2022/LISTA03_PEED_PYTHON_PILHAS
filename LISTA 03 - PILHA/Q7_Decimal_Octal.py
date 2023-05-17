from Pilha_Base import Pilha

def main(decimal):
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
decimal = int(input("Digite um número em decimal: "))
bin = main(decimal)
print("O número em Octal é: ")
for i in bin:
    print(i, end="")

