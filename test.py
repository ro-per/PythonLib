from Counter import *
from Matrix import *

counter = Counter()
matrix = Matrix(N=6, random=False)
print(matrix)

for (r, c) in matrix.iter_triangle('a'):
    matrix.data[r][c] = counter.inc()

print(matrix)

print("------------------------")
