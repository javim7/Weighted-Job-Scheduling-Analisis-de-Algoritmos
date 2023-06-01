'''
IMPLEMENTACION FUNCIONAL DEL ALGORITMO DE PROGRAMACION DINAMICA
'''
from functools import cmp_to_key
from Job import *

def jobComparator(s1, s2):
 
    return s1.finish < s2.finish
 
def latestNonConflict(arr, i):
 
    for j in range(i - 1, -1, -1):
        if arr[j].finish <= arr[i - 1].start:
            return j
 
    return -1
 
def scheduleDP(arr, n):
 
    # Sort jobs according to finish time
    arr = sorted(arr, key=cmp_to_key(jobComparator))
 
    # Create an array to store solutions of subproblems.
    # table[i] stores the profit for jobs till arr[i]
    # (including arr[i])
    table = [None] * n
    table[0] = arr[0].weight
 
    # Fill entries in M[] using recursive property
    for i in range(1, n):
 
        # Find profit including the current job
        inclProf = arr[i].weight
        l = latestNonConflict(arr, i)
 
        if l != -1:
            inclProf += table[l]
 
        # Store maximum of including and excluding
        table[i] = max(inclProf, table[i - 1])
 
    # Store result and free dynamic memory
    # allocated for table[]
    result = table[n - 1]
 
    return result