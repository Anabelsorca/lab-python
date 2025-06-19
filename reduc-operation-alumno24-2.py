#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import sys
import numpy as np
from numba import njit

def reduc_operation(a):
    x = 0
    for i in range(a):
        x += i
    return x

@njit
def reduc_with_loop_numba(arr):
    total = 0
    for i in arr:
        total += i
    return total

# Obtengo el valor desde argumentos de línea de comandos
if len(sys.argv) > 1:
    try:
        value = int(sys.argv[1])
    except ValueError:
        print("Error: el argumento debe ser un entero")
        sys.exit(1)
else:
    value = 1000000

print(f"\n Ejecutando reducción con value = {value}\n")

# Secuencial tradicional
start = time.time()
suma = reduc_operation(value)
end = time.time()
print(f"Time with plain Python loop: {end - start:.6f} seconds")
print(f"Resultado: {suma}")

# Listas
lista = list(range(value))

start = time.time()
suma_lista = sum(lista)
end = time.time()
print(f"Time with list + sum(): {end - start:.6f} seconds")

# NumPy
array = np.array(lista)

start = time.time()
suma_np = np.sum(array)
end = time.time()
print(f"Time with numpy + np.sum(): {end - start:.6f} seconds")

# Numba
start = time.time()
suma_numba = reduc_with_loop_numba(array)
end = time.time()
print(f"Time with Numba + loop: {end - start:.6f} seconds")
print(f"Resultado con Numba: {suma_numba}")

