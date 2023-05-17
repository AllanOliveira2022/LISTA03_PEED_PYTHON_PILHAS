class Item:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def adicionar(self, valor):
        item = Item(valor)
        item.proximo = self.topo
        self.topo = item
        self.tamanho += 1

    def remover(self):
        if self.topo is None:
            return None
        valor = self.topo.valor
        self.topo = self.topo.proximo
        self.tamanho -= 1
        return valor

    def is_empty(self):
        return self.topo is None
    def top(self):
        if self.topo is None:
            raise ValueError('A pilha está vazia')
        return self.topo.valor

    def tamanho(self):
        return self.tamanho
    
    def __len__(self):
        return self.tamanho()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.itens[-1]
'''class Item:
    def __init__(self,valor):
        self.valor = valor
        self.next = None

class Pilha:
    def __init__(self):
        self.top = None
        self.size = 0
    def adicionar(self,valor):
        novoItem = Item(valor)
        novoItem.next = self.top
        self.top = novoItem
        self.size += 1

    def remover(self):
        if self.size == 0:
            raise Exception("A pilha está vazia !!")
        valor = self.top.valor
        self.top = self.top.next
        self.size -= 1
        return valor

    def top(self):
        if self.size == 0:
            raise Exception("A pilha está vazia !!")
        return self.top.valor

    def is_empty(self):
        return self.size == 0

    def tamanho(self):
        return self.size
'''
            
