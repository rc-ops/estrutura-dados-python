class Fila:
    def __init__(self):
        self.lista_avioes = []

    def decolar_aviao(self):
        if self.listar_avioes():
            print(
                f"--> O avião nº {self.lista_avioes.pop()} acabou de decolar! <--")

    def adicionar_aviao(self, aviao):
        self.lista_avioes.append(aviao)
        print(f"--> Aviaõ nº {aviao} adicionado à fila com sucesso! <--")

    def listar_avioes(self):
        if (len(self.lista_avioes) == 0):
            print(
                "\033[031m--> Não há nenhum avião aguardando para decolagem! <--\033[m")
            return False
        else:
            print("")
            print("Lista de aviões:", end="")
            print(self.lista_avioes)
            print("")

        return True

    def listar_caracteristicas(self):
        if (len(self.lista_avioes) == 0):
            print(
                "\033[031m--> Não há nenhum avião aguardando para decolagem! <--\033[m")
        else:
            print(
                f"\033[031m--> O avião nº {self.lista_avioes[0]} não possui nenhuma característica cadastrada. <--\033[m")


def menu():
    fila = Fila()
    opcao = -1
    while opcao != 6:
        print("===================== Pista de decolagem =====================")
        print("Opções disponíveis: ")
        print("""
1 - Listar o número de aviões aguardando na fila de decolagem
2 - Autorizar a decolagem do primeiro avião da fila
3 - Adicionar um avião à fila de espera
4 - Listar todos os aviões na fila de espera
5 - Listar as características do primeiro avião da fila
6 - Sair
        """)
        opcao = int(input("Opção: "))

        if (opcao == 1):
            fila.listar_avioes()
        elif (opcao == 2):
            fila.decolar_aviao()
        elif (opcao == 3):
            try:
                aviao = int(
                    input("Insira o número do avião a ser adicionado: "))
                fila.adicionar_aviao(aviao)
            except:
                print("\033[031m--> Número inválido. Tente novamente. <--\033[m")
        elif (opcao == 4):
            fila.listar_avioes()
        elif (opcao == 5):
            fila.listar_caracteristicas()


menu()
