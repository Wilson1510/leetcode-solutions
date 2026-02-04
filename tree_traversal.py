from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self, level = 0):
        ret = "\t" * level + repr(self.val) + "\n"

        if self.left:
            ret += self.left.__str__(level + 1)
        if self.right:
            ret += self.right.__str__(level + 1)
        return ret


def level_order(root):
    queue = deque([root])
    urutan = []

    while queue:
        n = queue.popleft()
        urutan.append(n.val)

        if n.left: queue.append(n.left)
        if n.right: queue.append(n.right)
    print(urutan)

def preorder(root):
    result = []
    stack = []
    if root:
        stack.append(root)

    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
            
    print(result)

def inorder(root):
    current = root
    stack = []
    result = []

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.val)
        current = current.right

    print(result)
        
pohon = TreeNode(
    1,
    TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5, TreeNode(10), TreeNode(11))),
    TreeNode(3, TreeNode(6, TreeNode(12), TreeNode(13)), TreeNode(7, TreeNode(14), TreeNode(15)))
)

level_order(pohon)
preorder(pohon)
inorder(pohon)
