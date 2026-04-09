class ListNode:
    """Класс для узла односвязного списка."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def euclidean_gcd(a, b):
    """Алгоритм Евклида для нахождения НОД двух чисел."""
    
    a, b = abs(a), abs(b)
    while b > 0:
        a, b = b, a % b
    return a

def gcd_of_linked_list(head):
    """Находит НОД всех элементов односвязного списка."""
    if not head:
        return None  
    
    current_gcd = head.val
    current_node = head.next
    
    
    while current_node:
        current_gcd = euclidean_gcd(current_gcd, current_node.val)
        current_node = current_node.next
        
        
        if current_gcd == 1:
            break
            
    return current_gcd


head = ListNode(24)
head.next = ListNode(36)
head.next.next = ListNode(48)
head.next.next.next = ListNode(60)

result = gcd_of_linked_list(head)
print(f"НОД элементов списка: {result}")
