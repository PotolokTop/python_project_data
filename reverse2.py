# По нечетным строка, числа с отриц значением и перевод в положительную
import random
n = int(input(""))
matrix = []

for i in range(0,n):
    row = []
    for j in range(0,n):
        row.append(random.randint(0,10))
    matrix.append(row)

for row in matrix:
    print(row)

for i in range(n//2):
    if i % 2 != 0: # нечетные строки
        for j in range(n):
            if matrix[i][j] < 0:
                matrix[i][j] = 1/matrix[i][j]

for row in matrix:
    print(row)