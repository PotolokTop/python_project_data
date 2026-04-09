"""

Контрольная работа. Сапрыкин Даниил. Группа: ИС-24-2с Задача:
    
        1. Список. Найти max2 по величине. если list содержит меньше 2 значений, вывод сообщения 'меньше 2-ух'
        
"""

class LinkedList:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


head = LinkedList(3)
head.next = LinkedList(7)
head.next.next = LinkedList(5)
head.next.next.next = LinkedList(7)
head.next.next.next.next = LinkedList(2)


def second_max(head):  
    if head is None:
        return "Список пуст"

    max1 = None
    max2 = None
    current = head

    while current:
        if max1 is None or current.val > max1:
            if current.val != max1:
                max2 = max1
                max1 = current.val

        elif current.val != max1 and (max2 is None or current.val > max2):
            max2 = current.val

        current = current.next

    if max2 is None:
        return "Список содержит менее двух различных значений"

    return max2


print("Второе по величине число:", second_max(head))