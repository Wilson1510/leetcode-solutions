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
    # Runtime: 43ms
    # Memory Usage:22.1 MB
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            k -= 1
            if k == 0:
                return current.val
            current = current.right

    # Best time complexity solution (0ms)
    def kthSmallestBestTime(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        count = 0
        result = None

        # Void Function, implicitly returns "None" when
        # the line of code within the function is done
        def inorder(root: TreeNode) -> None:
            # Get variables from the parent function instead of overwriting it
            nonlocal count, result
            # Base case, for None values on recursion or result is now found
            if not root or result is not None:
                return

            # Traverse up to the leftmost, saving a whole pile of recursion
            inorder(root.left)
            count += 1
            if count == k:
                result = root.val # Assign val if count matches k
                return # Pile back up and base case handles the rest

            # Check the node's current right to avoid skipping it
            inorder(root.right)

        inorder(root)
        return result if result else 0

    # Best memory complexity solution (19MB)
    def kthSmallestBestMemory(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root):
            if not root:
                return 
            
            root.left = dfs(root.left)
            kth.append(root.val)
            root.right = dfs(root.right)
        
        kth = []
        dfs(root)
        return kth[k - 1]


if __name__ == "__main__":
    s = Solution()

    print(s.kthSmallest(TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4)), 1)) # 1
    print(s.kthSmallest(TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6)), 3)) # 3
    print(s.kthSmallest(TreeNode(1), 1)) # 1
