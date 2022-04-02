pilhaA = [1, 2, 3, 4, 5, 6]
pilhaB = [1, 2, 3, 4, 5, 6]

def recebe_duas_pilhas(pilha1, pilha2):
    if (pilha1 != pilha2):
        return "As pilhas são diferentes"
    else:
        return "As pilhas são iguais"

print(recebe_duas_pilhas(pilhaA, pilhaB))