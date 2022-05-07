class FilaSequencial:
    def __init__(self):
        self.fila = []

    def pesquisa_lista(self, numero):
        print(f"O número {numero} está presente na lista? ", end="")
        print(numero in self.fila)

    def inserir(self, numero):
        self.fila.append(numero)

    def remover(self, numero):
        print(f"O número {numero} self.fila.pop(numero foi removido da fila")

    def mostra_lista(self):
        print(self.fila)


fila = FilaSequencial()

fila.inserir(5)
fila.mostra_lista()
fila.inserir(676)
fila.inserir(12)
fila.mostra_lista()
fila.pesquisa_lista(5)
fila.pesquisa_lista(43)
