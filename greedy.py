'''
IMPLEMENTACION FUNCIONAL DEL ALGORITMO GREEDY
'''
from Job import *

def scheduleGreedy(job):
    job = sorted(job, key = lambda j: j.finish)  # Ordenar trabajos por tiempo de finalización

    n = len(job)
    result = []
    result.append(job[0])  # Añadir el primer trabajo

    i = 0
    for j in range(1, n):
        if job[j].start >= job[i].finish:  # Si el trabajo j no se superpone con i, añádelo a la lista
            result.append(job[j])
            i = j  # Actualizar el índice del último trabajo añadido
    return result  # Devolver la lista de trabajos