import os
from random import randint

class Les:
    def __init__(self, tamanho):
        self.t_max = tamanho
        self.quant = 0
        self.arquivo_nome = "numeros.txt"

    def imprimir(self):
        with open(self.arquivo_nome, "r") as arquivo:
            for linha in arquivo:
                print(linha.strip())

    def inserir(self, valor):
        with open(self.arquivo_nome, "a") as arquivo:
            arquivo.write(f"{valor}\n")
        self.quant += 1

    def escrever(self, bloco=1000000):
        with open(self.arquivo_nome, "w") as arquivo:
            for i in range(0, self.t_max, bloco):
                for _ in range(bloco):
                    if self.quant >= self.t_max:
                        break
                    numero = randint(0, self.t_max)
                    arquivo.write(f"{numero}\n")
                    self.quant += 1

    def buscar(self, valor):
        encontrados = 0
        with open(self.arquivo_nome, "r") as arquivo:
            for linha in arquivo:
                if linha.strip() == str(valor):
                    encontrados += 1
        return encontrados


