"""
Complexity:
- Time  : O()
- Space : O()
"""
# Belum selesai
from typing import Optional


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
    # Runtime: ms
    # Memory Usage: MB
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        parent = {}
        stack = [root]
        parent[root] = None

        while stack:
            node = stack.pop()

            if node.left:
                parent[node.left] = node
                stack.append(node.left)

            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        maxSum = float('-inf')

        for start in parent:
            stack = [(start, None, 0)]  # (node, prev, sum)

            while stack:
                node, prev, currSum = stack.pop()
                currSum += node.val
                maxSum = max(maxSum, currSum)

                for nxt in (node.left, node.right, parent[node]):
                    if nxt and nxt != prev:
                        stack.append((nxt, node, currSum))

        return maxSum

    # Best time complexity solution (ms)
    def maxPathSumBestTime(self, root: Optional[TreeNode]) -> int:
        pass

    # Best memory complexity solution (MB)
    def maxPathSumBestMemory(self, root: Optional[TreeNode]) -> int:
        pass


if __name__ == "__main__":
    s = Solution()

    print(s.maxPathSum(TreeNode(1, TreeNode(2), TreeNode(3)))) # 6
    print(s.maxPathSum(TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))) # 42
