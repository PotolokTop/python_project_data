import math
n = int(input("Введите n: "))
x = float(input("Введите x: "))
fact = 1 # значение факториала
result = 0 # хранения результата выражения

for i in range(1, n+1):
    fact = fact * i 
    result = result + (x**i) / (1*fact)
print(result)