# carros estacionados
pilha = [4932, 2423, 9877, 9999, 1000, 3443] 
placa_a_sair = 1000

def remove_carro(pilha, placa_desejada):
    carros_para_retirar = 0
    for p in pilha[::-1]:
        if p == placa_a_sair: # Caso o carro esteja estacionado
            indice = pilha.index(p)
            return pilha[indice+1:]
        else:
            carros_para_retirar += 1
    
    print("Não existe carro com tal placa")

print(remove_carro(pilha, placa_a_sair))