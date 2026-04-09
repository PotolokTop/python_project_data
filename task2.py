# 3 вариант
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def product_of_leaves(root):
    if root is None:
        return 1
    
    if root.left is None and root.right is None:
        return root.value
    
 
    left_product = product_of_leaves(root.left)
    right_product = product_of_leaves(root.right)
    
    return left_product * right_product




root = Node(10)
root.left = Node(5)
root.right = Node(3)

root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(6)

print(product_of_leaves(root)) 