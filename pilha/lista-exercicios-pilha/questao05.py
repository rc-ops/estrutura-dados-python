pilha = [0, 15, 15, -5, 9, 12, 26]

# Itera invertido, que por coincidência é a ordem da pilha
for n in pilha[::-1]:
    if n > 0:
        print(n, end = " ")
