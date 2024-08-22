import time
import Les
import sys
import psutil
from collections.abc import Iterable

def deep_getsizeof(obj, seen=None):
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    seen.add(obj_id)
    
    if isinstance(obj, dict):
        size += sum([deep_getsizeof(v, seen) for v in obj.values()])
        size += sum([deep_getsizeof(k, seen) for k in obj.keys()])
    elif isinstance(obj, list) or isinstance(obj, tuple) or isinstance(obj, set):
        size += sum([deep_getsizeof(i, seen) for i in obj])
    return size

def medir_cpu_durante_execucao(funcao, *args, **kwargs):
    processo = psutil.Process()
    inicio_cpu = processo.cpu_percent(interval=None)
    resultado = funcao(*args, **kwargs)
    fim_cpu = processo.cpu_percent(interval=None)
    uso_cpu = fim_cpu - inicio_cpu
    return resultado, uso_cpu

def gerar(quantidade):
    les = Les.Les(quantidade)
    les.escrever(bloco=10**6)  # Escrever em blocos de 1 milhão
    return "[OK] Tarefa concluída."

def buscar(numero):
    inicio = time.time()
    les = Les.Les(tamanho=10**12)  # Criar um objeto Les com tamanho de 1 trilhão
    encontrados, uso_cpu = medir_cpu_durante_execucao(les.buscar, numero)
    fim = time.time()
    diferenca = fim - inicio
    memoria_gasta = deep_getsizeof(les) / (1024 ** 2)  # Converte para Megabytes
    
    print(f"Número de ocorrências encontradas: {encontrados}")
    print(f"Tempo de execução: {diferenca:.2f} segundos")
    print(f"Memória RAM usada: {memoria_gasta:.2f} MB")
    print(f"Porcentagem de CPU usada: {uso_cpu:.2f}%")

quantidade = int(input("[!] Insira a quantidade de caracteres -> "))
resultado, uso_cpu_gerar = medir_cpu_durante_execucao(gerar, quantidade)
print(resultado)
print(f"Porcentagem de CPU usada durante a geração: {uso_cpu_gerar:.2f}%")
numero_procurado = int(input("[!] Insira o número que deseja buscar -> "))
buscar(numero_procurado)
