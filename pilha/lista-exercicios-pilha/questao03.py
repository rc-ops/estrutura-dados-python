pilha = []
vetor = [1, 5, 6, 9, 10, 12]
def preenche_pilha(pilha, vetor):
    for i in vetor[::-1]:
        pilha.append(i)

preenche_pilha(pilha, vetor)
print(pilha)