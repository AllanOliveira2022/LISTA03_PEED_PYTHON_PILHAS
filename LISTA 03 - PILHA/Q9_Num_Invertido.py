from Pilha_Base import Pilha

def inverter(frase):
    pilha = Pilha()
    string = frase
    for digito in string:
        pilha.adicionar(digito)
    novo_num = ''
    while not pilha.is_empty():
        pilha.top()
        novo_num += pilha.top() + ""
        pilha.remover()

    return novo_num
Num = input("Digite um número: ")
Num_invertido = inverter(Num)
print("Número normal: ")
print(Num)
print("Número invertido: ")
print(Num_invertido)
if Num == Num_invertido :
    print("O número é um palíndromo !")
else:
    print("O número NÃO é um palíndromo !!")    