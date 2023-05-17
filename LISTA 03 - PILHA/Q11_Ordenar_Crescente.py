from Pilha_Base import Pilha
def ordenar_lista(lista):
    listaint=[]
    for i in lista:
        listaint.append(int(i))
        
    pilha = Pilha()
    lista_ordenada = []


    for num in listaint:
        pilha.adicionar(num)

    while not pilha.is_empty():
        elemento = pilha.remover()
        posicao = 0
        while posicao < len(lista_ordenada) and elemento > lista_ordenada[posicao]:
            posicao += 1
        lista_ordenada.insert(posicao, elemento)

    return lista_ordenada

numeros = input("Digite os números separado por espaços: ").split()
numeros_ordenados = ordenar_lista(numeros)
print("Números ordenados:", numeros_ordenados)