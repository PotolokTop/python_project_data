# Вариант 5 

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def pre_order_sum_primes(node):
    if node is None:
        return 0
    total = 0
    if is_prime(node.value):
        total += node.value
    total += pre_order_sum_primes(node.left)
    total += pre_order_sum_primes(node.right)
    return total

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(6)
    root.right.right = TreeNode(17)

    result = pre_order_sum_primes(root)
    print("Сумма простых чисел:", result)