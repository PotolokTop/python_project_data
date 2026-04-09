class TreeNode:
    """Класс для узла бинарного дерева."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def post_order_leaves_product(root):
    """Выполняет post-order обход и возвращает произведение листьев."""
    product = 1
    has_leaves = False  
    
    def post_order_traverse(node):
        nonlocal product, has_leaves
        if not node:
            return
        
        post_order_traverse(node.left)
        
        post_order_traverse(node.right)
        
        if node.left is None and node.right is None:
            product *= node.val
            has_leaves = True

    post_order_traverse(root)
    
    return product if has_leaves else 0


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)

result = post_order_leaves_product(root)
print(f"Произведение листьев дерева: {result}")