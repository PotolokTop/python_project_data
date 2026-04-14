# Структуры данных
from dataclasses import dataclass # библиотека для авто-генерации методов __init__ и читаемости структуры

@dataclass
class Product:
    id: int # идентификатор
    name: str # название
    price: float # цена
    quantity: int # количество

# список товаров
products = [
    Product(1, "Bread", 150, 5), 
    Product(2, "Milk", 250, 10),
    Product(3, "Cheese", 750, 3),
]

# 1) общая стоимость склада
sum = 0
for p in products:
    sum = sum + p.price
print("Сумма склада: ", sum)

# 2) самый дорогой товар
most_expensive = max(products, key=lambda p: p.price)
print("Самый дорогой товар: ", most_expensive.name)

# 3) фильтрация товаров дешевле n цены
n = 500
for p in products:
    if p.price < n:
        print(p.name)