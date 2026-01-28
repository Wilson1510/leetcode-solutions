"""
Complexity:
- Time  : O(n)
- Space : O(n)
"""
from typing import Optional
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


class Solution:
    # Runtime: 0ms
    # Memory Usage: 19.5MB
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        antrian = deque([root])
        while antrian:
            node = antrian.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                antrian.append(node.left)
            if node.right:
                antrian.append(node.right)
        return root

    # Best time complexity solution (0ms)
    def invertTreeBestTime(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
    
        queue = [root]

        while len(queue) > 0:
            # Pop at first index
            node = queue.pop(0)
            # Invert branches of current node
            node.left, node.right = node.right, node.left

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        
        return root

    # Best memory complexity solution (16.9MB)
    def invertTreeBestMemory(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        q = deque([root])
        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return root


if __name__ == "__main__":
    s = Solution()

    n = TreeNode(4)
    n.left = TreeNode(2, TreeNode(1), TreeNode(3))
    n.right = TreeNode(7, TreeNode(6), TreeNode(9))

    print(s.invertTree(n)) # [4,7,2,9,6,3,1]
    print(s.invertTree(TreeNode(2, TreeNode(1), TreeNode(3)))) # TreeNode(2, TreeNode(3), TreeNode(1))
    print(s.invertTree(None)) # None
