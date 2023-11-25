import time
import random

def bubble_sort(arr):
    n = len(arr)
    swaps = 0

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1

    return swaps


def generate_data(size, case):
    if case == "Melhor Caso":
        return list(range(1, size+1))
    elif case == "Pior Caso":
        return list(range(size, 0, -1))
    elif case == "Caso Médio":
        return random.sample(range(1, size+1), size)


sizes = [1000, 10000, 100000]
cases = ["Melhor Caso", "Pior Caso", "Caso Médio"]

for size in sizes:
    for case in cases:
        data = generate_data(size, case)

        data_copy = data.copy()

        start_time = time.time()
        swaps = bubble_sort(data_copy)
        end_time = time.time()

        print(f"Tamanho: {size} | Caso: {case} | Tempo: {end_time - start_time:.6f} segundos | Trocas: {swaps}")
