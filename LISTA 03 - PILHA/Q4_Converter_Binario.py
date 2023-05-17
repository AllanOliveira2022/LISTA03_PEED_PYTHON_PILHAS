from Pilha_Base import Pilha

def main(decimal):
    pilha = Pilha()
    num = decimal
    for n in range(0,num):
        resto = num % 2 
        num = num // 2
        pilha.adicionar(resto)
        print("O resto é: ",resto)
        print("Resto da divisão:",num)
        if num == 1:
            break
    if not num % 2 == 0:
        pilha.adicionar(1)
    
    binario = []
    while not pilha.is_empty():
        pilha.top()
        binario.append(pilha.top())
        pilha.remover()

    return binario
decimal = int(input("Digite um número: "))
bin = main(decimal)
print("O número em binário é: ")
for i in bin:
    print(i, end="")

