pilhaNegativos = []
pilhaPositivos = []
vetor = [1, 2, -1, -2, 0, 3, -3]


def TPilha2(pilha1, pilha2, vetor):
    for n in vetor[::-1]:
        if n > 0:
            pilhaPositivos.append(n)
        elif n < 0:
            pilhaNegativos.append(n)
        else:
            pilhaNegativos.pop()
            pilhaPositivos.pop()

    print(pilhaPositivos)
    print(pilhaNegativos)


TPilha2(pilhaNegativos, pilhaPositivos, vetor)
