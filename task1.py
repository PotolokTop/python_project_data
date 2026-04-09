# 2 вариант

import math

class LinkedList:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


head = LinkedList(1)
head.next = LinkedList(2)
head.next.next = LinkedList(4)
head.next.next.next = LinkedList(9)
head.next.next.next.next = LinkedList(5)


# функция подсчёта точных квадратов
def fafa(head):
    current = head
    count = 0

    while current:
        root = int(math.sqrt(current.val))
        if root * root == current.val:
            count += 1
        current = current.next

    return count


# проверка
print(fafa(head))