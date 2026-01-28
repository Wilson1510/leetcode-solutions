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
    # Memory Usage: 20.32MB
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        max_depth = 0

        while queue:
            max_depth += 1

            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        return max_depth

    # Best time complexity solution (0ms)
    def maxDepthBestTime(self, root: Optional[TreeNode]) -> int:
        def dfs(curr):
            if not curr:
                return 0
            return 1 + max(dfs(curr.left), dfs(curr.right))
        return dfs(root)

    # Best memory complexity solution (17.7MB)
    def maxDepthBestMemory(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        leftmax=self.maxDepth(root.left)
        rightmax=self.maxDepth(root.right)
        return (max(rightmax,leftmax)+1)


if __name__ == "__main__":
    s = Solution()

    print(s.maxDepth(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4))))) # 3
    print(s.maxDepth(None)) # None
