import heapq as hq

class FilaPrioridade:
    def __init__(self):
        self.lista = []

    def inserir_elemento(self, numero):
        hq.heappush(self.lista, numero)
        hq.heapify(self.lista)

    def remover_elemento(self):
        hq.heappop(self.lista)
        hq.heapify(self.lista)


fila = FilaPrioridade()

fila.inserir_elemento(999)
fila.inserir_elemento(1)
fila.inserir_elemento(9)
fila.inserir_elemento(10)
fila.inserir_elemento(12)
fila.inserir_elemento(34)
fila.inserir_elemento(55)

print(f"Lista inicial: {fila.lista}")
fila.remover_elemento()
print(f"1ª remoção: {fila.lista}")
fila.remover_elemento()
print(f"2ª remoção: {fila.lista}")
fila.remover_elemento()
print(f"3ª remoção: {fila.lista}")