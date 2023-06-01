from greedy import *
from Job import *
from dp import *

# Ejemplo de uso:
jobs = [Job(1, 2, 50), Job(3, 10, 20), Job(6, 19, 100), Job(2, 100, 200)]

# Algoritmo programacion dinamica
print(scheduleDP(jobs, len(jobs)))  

# Algoritmo greedy
scheduled_jobs = scheduleGreedy(jobs)
for job in scheduled_jobs:
    print(f"Start: {job.start}, Finish: {job.finish}, Weight: {job.weight}")