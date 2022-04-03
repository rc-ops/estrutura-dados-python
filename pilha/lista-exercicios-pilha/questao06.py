vetor = [4, 2, 3, 4, 5, 6, 7, 8, 9, 22, 11, 12, 13, 14, 18]
pilha = []


def TPilha(vetor):
    if len(vetor) < 15:
        print("É necessário um vetor contendo 15 elementos.")

    for n in vetor[::-1]:
        if n % 2 == 0:
            pilha.append(n)
        else:
            pilha.pop()

    for i in range(len(pilha)):
        i = 0  # Remove a partir do topo
        if len(pilha) > 0:
            print(pilha.pop(i))

    print(pilha)


TPilha(vetor)
