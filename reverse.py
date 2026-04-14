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
    
for i in range(n//2): # проходимся по половине чтобы не делать обмен два раза
        if i % 2 == 0: # четные строки
            for j in range(n):
                temp = matrix[i][j] # 3 переменная
                matrix[i][j] = matrix[n - i - 1][j] # не забываем второй индекс j при обращении к элементу
                matrix[n - i - 1][j] = temp

print("результат:")       
for row in matrix:
    print(row)

# a = [1,2,3,4,5]

# for i in range(len(a)//2):
#     temp = a[i]
#     # print(a[len(a)-i-1])
#     a[i] = a[len(a)-i-1]
#     a[len(a)-i-1] = temp

# print(a)
