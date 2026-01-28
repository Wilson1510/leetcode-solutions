"""
Complexity:
- Time  : O()
- Space : O()
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
    # Runtime: ms
    # Memory Usage: MB
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pass

    # Best time complexity solution (ms)
    def invertTreeBestTime(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pass

    # Best memory complexity solution (MB)
    def invertTreeBestMemory(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pass


if __name__ == "__main__":
    s = Solution()
