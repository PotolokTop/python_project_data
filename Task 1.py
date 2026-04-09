# Вариант 5

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Функция поиска второго по величине числа
def second_largest(head):
    if not head or not head.next:
        return "Список содержит менее двух элементов"
    
    unique_values = set()
    current = head
    while current:
        unique_values.add(current.value)
        current = current.next

    if len(unique_values) < 2:
        return "Список содержит менее двух различных значений"
    
    sorted_values = sorted(unique_values, reverse=True)
    return sorted_values[1]

# Пример использования
if __name__ == "__main__":
    # создаем список: 3 -> 1 -> 4 -> 4 -> 2
    head = Node(3)
    head.next = Node(1)
    head.next.next = Node(4)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    result = second_largest(head)
    print("Второе по величине число:", result)