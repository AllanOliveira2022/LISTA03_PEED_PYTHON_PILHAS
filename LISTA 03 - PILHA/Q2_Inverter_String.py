from Pilha_Base import Pilha

def inverter(frase):
    pilha = Pilha()
    fraseLista = frase.split()   
    for palavra in fraseLista:
        pilha.adicionar(palavra)
    nova_frase = ''
    while not pilha.is_empty():
        pilha.top()
        nova_frase += pilha.top() + " "
        pilha.remover()

    return nova_frase
frase = input("Digite uma frase: ")
nova_frase = inverter(frase)
print("Frase normal: ")
print(frase)
print("Frase invertida: ")
print(nova_frase)
   