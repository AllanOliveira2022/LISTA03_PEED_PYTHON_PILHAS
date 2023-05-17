from Pilha_Base import Pilha

def inverter(frase):
    pilha = Pilha()
    string = frase
    for letra in string:
        pilha.adicionar(letra)
    nova_frase = ''
    while not pilha.is_empty():
        pilha.top()
        nova_frase += pilha.top() + ""
        pilha.remover()

    return nova_frase
palavra = input("Digite uma Palavra: ")
nova_palavra = inverter(palavra)
print("Palavra normal: ")
print(palavra)
print("Palavra invertida: ")
print(nova_palavra)
if palavra == nova_palavra :
    print("A palavra é um palíndromo !")
else:
    print("A palavra NÃO é um palíndromo !!")    