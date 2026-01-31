"""
Complexity:
- Time  : O(n)
- Space : O(n)
"""
from typing import Optional
from collections import deque
from math import inf


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
    # Memory Usage: 20.87MB
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root, float('-inf'), float('inf'))])

        while queue:
            n, minimum, maximum = queue.popleft()

            if not (minimum < n.val < maximum):
                return False
            
            if n.left:
                queue.append((n.left, minimum, n.val))

            if n.right:
                queue.append((n.right, n.val, maximum))

        return True

    # Best time complexity solution (0ms)
    prev = None
    def isValidBSTBestTime(self, root: Optional[TreeNode]) -> bool:
        def helper(root, low, high):     
            if root is None:
                return True                
            if root.val <= low or root.val >= high:
                return False 
            
            return helper(root.left, low, root.val) & helper(root.right, root.val, high)
      
      
      
        if root.left is not None and (root.left.val >= root.val):

            return False          
        if root.right is not None and (root.right.val <= root.val):

            return False
        return helper(root.left, -inf, root.val) & helper(root.right, root.val, inf)


    # Best memory complexity solution (18.2MB)
    def isValidBSTBestMemory(self, root: Optional[TreeNode], min_val=-2**31-1, max_val=2**31) -> bool:
        if root is None:
            return True
        
        if not (min_val < root.val < max_val):
            return False
        
        return self.isValidBST(root.left, min_val, root.val) and self.isValidBST(root.right, root.val, max_val)


if __name__ == "__main__":
    s = Solution()

    print(s.isValidBST(TreeNode(2, TreeNode(1), TreeNode(3)))) # True
    print(s.isValidBST(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))))) # False
