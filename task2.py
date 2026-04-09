"""

Контрольная работа. Сапрыкин Даниил. Группа: ИС-24-2с Задача:
    
        2. Бинарное дерево. Pre-order обход. Найти сумму всех узлов. значения оявляется простым числом. Если узлов нет, вывести 'дерево пустое'
        
"""


class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(6)
root.right.right = TreeNode(11)


class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, val):
        self.stack.append(val)
        
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    	
    def peek(self):
        if not self.is_empty():
            return self.stack[len(self.stack) - 1]


def is_prime(num):
    if num < 2: 
        return False
    
    for i in range(2,num):
        if num % i == 0:
            return False
    
    return True


def pre_order(root):
    if root is None:
        return "Пусто"

    stack = Stack()
    result = []
    prime_sum = 0   

    stack.push(root)

    while stack.is_empty() == False:
        current = stack.pop()
        result.append(current.val)

        if is_prime(current.val):
            prime_sum += current.val

        if current.right:
            stack.push(current.right)
        if current.left:
            stack.push(current.left)

    print("Pre-order:", result)
    return prime_sum


print("Сумма:", pre_order(root))