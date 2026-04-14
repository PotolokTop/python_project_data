# Variant № 4
from math import gcd

class LinkedList:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def HOD(a, b):
    return gcd(a, b)
def HOD_linked_list(head):
    if head is None:
        return 0

    result = head.val
    current = head.next

    while current:
        result = HOD(result, current.val)
        current = current.next
    return result

head = LinkedList(2)
head.next = LinkedList(3)
head.next.next = LinkedList(12)

print(HOD_linked_list(head))