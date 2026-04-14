#создание n на n матрицы из рандомных элементов с диапазоном от 0 д 100
import random
rows = int(input("Строки: "))
cols = int(input("Столбцы: "))

matrix = [] # список строк

for i in range(rows):
    row = [] # создаем строку элементов
    for j in range(cols):
        row.append(random.randint(0,100))
    matrix.append(row) #добавляем строку в матрицу

for row in (matrix):
    print(row)