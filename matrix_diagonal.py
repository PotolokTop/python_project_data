# нахождение суммы элементов диагонали матрицы
import random
rows = int(input("rows: "))
cols = int(input("columns: "))
matrix = []
elements = []

# заполняем матрицу
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(0, 100))
    matrix.append(row)

# выводим матрицу
for row in (matrix):
    print(row)

# проходимся по матрице
for i in range(rows):
    for j in range(cols):
        if i == j: # сравниваем i и j индексы
            elements.append(matrix[i][j]) 

summ = 0 # хранение результата

# суммируем каждый элемент в диагонали
for i in range(len(elements)):
    summ += elements[i]

print(summ)

