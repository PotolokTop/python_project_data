# Variant № 4
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.right = TreeNode(3)

def in_order(root):
    stack = []
    result = []
    current = root
    
    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result

print(in_order(root))

def is_bst(root):
    val = in_order(root)

    for i in range(1, len(val)):
        if val[i] <= val[i - 1]:
            return False
    return True

print(is_bst(root))