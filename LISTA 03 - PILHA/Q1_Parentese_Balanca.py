from Pilha_Base import Pilha
def main():
    pilha = Pilha()
    expressao = []
    expressao = str(input("Digite uma expressão com parênteses: "))
    for valor in expressao:
        if valor == "(":
            pilha.adicionar(valor)
        if valor == ")":
            pilha.remover()
    if pilha.is_empty() == True:
        print("os parenteses estão balanceados !")
    else:
        print("Os parenteses estão desbalanceados !")  

if __name__ == "__main__":
    main()    


