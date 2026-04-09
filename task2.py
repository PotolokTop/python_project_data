# 2 вариант 

class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)


def fafa(root):
    if not root:
        return 0

    stack = [root]
    result = 0
    sign = 1  # +1, потом -1, потом +1...

    while stack:
        current = stack.pop()

        result += sign * current.val
        sign *= -1

        # сначала кладём правого, потом левого
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return result


# проверка
print(fafa(root))