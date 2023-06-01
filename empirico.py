from greedy import *
from Job import *
from dp import *
import timeit
import random
import matplotlib.pyplot as plt
import numpy as np


'''
Listado de entradas de prueba
'''
sizes = [50 + i*500 for i in range(30)]
dp_times = []
greedy_times = []

# realizando las pruebas
for n in sizes:
    jobs = [Job(random.randint(1, 100), random.randint(101, 200), random.randint(1, 500)) for _ in range(n)]

    # Algoritmo programacion dinamica
    start_time = timeit.default_timer()
    scheduleDP(jobs, len(jobs))
    end_time = timeit.default_timer()
    dp_times.append(end_time - start_time)

    # Algoritmo greedy
    start_time = timeit.default_timer()
    scheduleGreedy(jobs)
    end_time = timeit.default_timer()
    greedy_times.append(end_time - start_time)


'''
Plot de los resultados sin regresion logistica
'''

# Plotting de programacion dinamica
plt.figure(figsize=(10,5))
plt.scatter(sizes, dp_times, color='r', label='Programación Dinámica')
plt.title('Tiempo de ejecución: Programación Dinámica')
plt.xlabel('Tamaño de entrada (n)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.legend()
plt.grid(True)
plt.show()

# plot de algoritmo greedy
plt.figure(figsize=(10,5))
plt.scatter(sizes, greedy_times, color='b', label='Greedy')
plt.title('Tiempo de ejecución: Algoritmo Greedy')
plt.xlabel('Tamaño de entrada (n)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.legend()
plt.grid(True)
plt.show()

# plot de comparacion
plt.figure(figsize=(10,5))
plt.scatter(sizes, dp_times, color='r', label='Programación Dinámica')
plt.scatter(sizes, greedy_times, color='b', label='Greedy')
plt.title('Comparación de tiempos de ejecución')
plt.xlabel('Tamaño de entrada (n)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.legend()
plt.grid(True)
plt.show()


'''
Plot de los resultados con regresion lineal
'''

# Perform polynomial regression for Dynamic Programming
dp_coeffs = np.polyfit(sizes, dp_times, 2)  # Change degree to 2 for polynomial fit
dp_func = np.poly1d(dp_coeffs)

# Perform polynomial regression for Greedy
greedy_coeffs = np.polyfit(sizes, greedy_times, 2)  # Change degree to 2 for polynomial fit
greedy_func = np.poly1d(greedy_coeffs)

print("Función de regresión polinomial para Programación Dinámica:")
print(dp_func)
print("\nFunción de regresión polinomial para Greedy:")
print(greedy_func)

# Plotting the data and polynomial regression for Dynamic Programming
plt.figure(figsize=(10,5))
plt.scatter(sizes, dp_times, color='r', label='Programación Dinámica')
plt.plot(sizes, dp_func(sizes), color='r')
plt.title('Tiempo de ejecución: Programación Dinámica')
plt.xlabel('Tamaño de entrada (n)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.legend()
plt.grid(True)
plt.show()

# Plotting the data and polynomial regression for Greedy Algorithm
plt.figure(figsize=(10,5))
plt.scatter(sizes, greedy_times, color='b', label='Greedy')
plt.plot(sizes, greedy_func(sizes), color='b')
plt.title('Tiempo de ejecución: Algoritmo Greedy')
plt.xlabel('Tamaño de entrada (n)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.legend()
plt.grid(True)
plt.show()