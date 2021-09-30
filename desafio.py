import random
random_list = []
d = 500000

# criando a lista com números aleatórios
for i in range(d):
    random_list.append(random.randint(0, d))

# funções do algoritmo Merge Sort 
def ordenar(array):
    ordenar_metade(array, 0, len(array) - 1)


def ordenar_metade(array, comeco, fim):
    if comeco >= fim:
        return

    meio = (comeco + fim) // 2

    ordenar_metade(array, comeco, meio)
    ordenar_metade(array, meio + 1, fim)

    merge(array, comeco, fim)


def merge(array, comeco, fim):
    array[comeco: fim + 1] = sorted(array[comeco: fim + 1])

# Executando merge sort na lista
ordenar(random_list)
