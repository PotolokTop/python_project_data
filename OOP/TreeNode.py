class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# pre-order 
def pre_order(root):
    stack = [root]
    result = [] # result array

    while stack: # while stack not empty
        node = stack.pop() # last added node
        result.append(node.val)

        if node.right:
            stack.append(node.right) # following LIFO starting from right to append left
        if node.left:
            stack.append(node.left)
    
    return result

# print(pre_order(root))

# in-order
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

# print(in_order(root))

# post-order
def post_order (root):
    stack1 = [root]
    stack2 = []
    result = []

    while stack1: 
        node = stack1.pop() # узел последний из stack1 
        stack2.append(node) # кладем его в stack2  
        
        if node.left: 
            stack1.append(node.left) # записываем элемент слева
        if node.right:
            stack1.append(node.right)
        
    while stack2:
        node = stack2.pop()
        result.append(node.val)

    return result

# print(post_order(root))

# pre-order two trees equality
def checkEqual(p, q):
    stack1 = [p.root]
    result1 = [] # result p
    result2 = [] # result q

    # if p.root.val == q.root.val:
        # stack = p.root

    while stack:
        node = stack.pop() # last added node
        result.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


    
    return result