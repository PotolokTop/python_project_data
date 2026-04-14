# Вариант 4 Филин Леонид задание 2
class TreeNode: # класс дерева TreeNode
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# проверка на корректность
def is_valid_bst(root):
    stack = []
    current = root
    prev = None

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()

        if prev is not None and current.val <= prev:
            return False

        prev = current.val
        current = current.right

    return True


# пример BST
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

print(is_valid_bst(root))   # вывод True