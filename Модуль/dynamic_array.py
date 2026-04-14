# динамический массив с автоматическим увеличением в 2 раза
class DynamicArray:
    # Конструктор
    def __init__(self):
        self.capacity = 1 # текущий размер выделенной памяти
        self.size = 0 #количество элементов
        self.data = [None] * self.capacity # определяем пустой массив

    # Методы
        
    # добавление элемента
    def append(self, value):
        if self.size == self.capacity: # если массив заполнен
            self._resize() # обращаемся к resize()
        
        self.data[self.size] = value # присваиваем элемент в качестве ПОСЛЕДНЕГО элемента (self.size)
        self.size += 1 # обновляем количество элементов

    # увеличение массива
    def _resize(self):
        self.capacity *= 2 # увеличиваем текущий размер
        newData = [None] * self.capacity # обновляем фактическую вместимость массива

        # собираем массив в newData
        for i in range(self.size):
            newData[i] = self.data[i]

        self.data = newData # присваиваем собранный массив

# Создание экземпляра массива и добавление в него элементов
array1 = DynamicArray()

array1.append(10)
array1.append(20)
array1.append(30)

print(array1.data)
