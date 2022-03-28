import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.valores = np.chararray(self.capacidade, unicode = True)
        self.topo = -1
    
    def pilha_vazia(self):
        if self.topo == -1:
            return True 
        else:
            return False
        
    def pilha_cheia(self):
        if self.topo == self.capacidade-1:
            return True
        else:
            return False

    def empilhar(self, valor):
        if self.pilha_cheia():
            print("A pilha já está cheia.")
        else:
            self.topo += 1 
            self.valores[self.topo] = valor 

    
    def desempilhar(self): 
        if self.pilha_vazia():
            print("A pilha já está vazia.")
        else:
            self.topo -= 1 
            # valor = self.valores[self.topo]
            # return valor
            
    def ver_topo(self):
        if self.topo != -1:
            return self.valores[self.topo]
        else:
            return -1

    def validacao(self, f):    
        stack = []
        x = 0
        while x < len(f):
            if f[x] == "(":
                stack.append("(")

            if f[x] == "[":
                stack.append("[")

            if f[x] == "{":
                stack.append("{")

            if f[x] == ")":
                if len(stack) > 0:
                    top = stack.pop()
                else:
                    stack.append(")")  
                    break

            if f[x] == "]":
                if len(stack) > 0:
                    top = stack.pop()
                else:
                    stack.append("]") 
                    break

            if f[x] == "}":
                if len(stack) > 0:
                    top = stack.pop()
                else:
                    stack.append("}") 
                    break
            x += 1

        if len(stack) == 0:
            return True
        else:
            return False

frase = str(input("Digite a sequência de caracteres a validar:"))
quantidade = len(frase)
pilha = Pilha(quantidade)
print(f"A expressão é válida? {pilha.validacao(frase)}")
