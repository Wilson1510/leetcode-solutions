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
    # Memory Usage: 19.57MB
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p, q)])

        while queue:
            n1, n2 = queue.popleft()
            if not n1 and not n2:
                continue
            
            if not n1 or not n2 or (n1.val != n2.val):
                return False
            
            queue.append((n1.left, n2.left))
            queue.append((n1.right, n2.right))

        return True

    # Best time complexity solution (0ms)
    def isSameTreeBestTime(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        return False

    # Best memory complexity solution (16.7MB)
    def isSameTreeBestMemory(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Lets think through this
        #   I need to find a way to check each node of each tree and see if they are equal. I can use a BFS for this or a DFS
        #For this, I will use a BFS. 
        if p is None and q is None:
            return True
        elif None in [p, q]:
            return False
        elif p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    s = Solution()

    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    print(s.isSameTree(p, q)) # True

    p = TreeNode(1, TreeNode(2))
    q = TreeNode(1, None, TreeNode(2))
    print(s.isSameTree(p, q)) # False

    p = TreeNode(1, TreeNode(2), TreeNode(1))
    q = TreeNode(1, TreeNode(1), TreeNode(2))
    print(s.isSameTree(p, q)) # False
    print(s.isSameTree(TreeNode(1), TreeNode(1, None, TreeNode(2))))
