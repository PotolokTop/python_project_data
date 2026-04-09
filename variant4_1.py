# Вариант 4 Филин Леонид задание 1
import math

class ListNode: # класс ListNode
    def __init__(self, val=0, next=None):
        self.val = val # значение
        self.next = next # ссылка на следующий элемент


# создание списка
def create_list(arr):
    head = ListNode(arr[0])
    current = head

    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next

    return head


# НОК всех элементов списка
def lcm_list(head):
    if not head:
        return 0

    result = head.val
    current = head.next

    while current:
        # result = lcm(result, current.val)
        result = abs(result*current.val)//math.gcd(result,current.val)
        current = current.next

    return result

arr = [4, 6, 8] # создание массива под LinkedList
head = create_list(arr) # создаем LinkedList

print("НОК списка:", lcm_list(head))