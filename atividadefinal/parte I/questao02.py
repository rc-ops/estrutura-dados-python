# carros estacionados
pilha = [4932, 2423, 9877, 9999, 1000, 3443] 
placa_a_sair = 2423

def remove_carro(pilha, placa_a_sair):
    carros_para_retirar = []
    for p in pilha[::-1]:
        if p == placa_a_sair: # Caso o carro esteja estacionado
            return carros_para_retirar
        else:
            carros_para_retirar.append(p)
    
    print("Não existe carro com tal placa")

print(f"Carros a saírem: {remove_carro(pilha, placa_a_sair)}")