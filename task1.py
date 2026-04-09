# 3  вариант

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node(48)
head.next = Node(18)
head.next.next = Node(30)
head.next.next.next = Node(12)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def gcd_list(head):
    if head is None:
        return 0
    
    result = head.value
    current = head.next
    
    while current:
        result = gcd(result, current.value)
        current = current.next
    
    return result

print(gcd_list(head))  

