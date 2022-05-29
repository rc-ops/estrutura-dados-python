from random import randint
soldados = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def circulo_soldados(numero_chapeu, soldado_escolhido):
    if len(soldados) > 1:
        if numero_chapeu > soldado_escolhido:
            for x in range(len(soldados)):
                if x == numero_chapeu:
                    print(f"Foi removido o soldado {soldados.pop(x)}")
        else:
            for x in range(len(soldados), -1, -1):
                if x == numero_chapeu:
                    print(f"Foi removido o soldado {soldados.pop(x-1)}")

        numero_chapeu = randint(0, len(soldados)+1)
        soldado_escolhido = numero_chapeu+1
        # Recursividade
        circulo_soldados(numero_chapeu, soldado_escolhido)

    else:
        print(f"Soldado restante: {soldados}")



numero_chapeu = randint(0, len(soldados) + 1)
soldado_escolhido = randint(0, len(soldados)+1)

if numero_chapeu == soldado_escolhido:
    soldado_escolhido = soldado_escolhido + 1

circulo_soldados(numero_chapeu, soldado_escolhido)