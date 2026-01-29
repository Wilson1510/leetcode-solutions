"""
Complexity:
- Time  : O(n * m) m is the number of node of subroot
- Space : O(n + m)
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
    # Memory Usage: 19.6MB
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(r, sr):
            checking = deque([(r, sr)])

            while checking:
                rc, src = checking.popleft()

                if not rc and not src:
                    continue

                if not rc or not src or rc.val != src.val:
                    return False
                
                checking.append((rc.left, src.left))
                checking.append((rc.right, src.right))

            return True

        queue = deque([root])

        while queue:
            r = queue.popleft()

            if check(r, subRoot):
                return True
            
            if r.left: queue.append(r.left)
            if r.right: queue.append(r.right)

        return False

    # Best time complexity solution (0ms)
    def isSubtreeBestTime(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(root):
            if not root:
                return "#"
            return f"^{root.val},{serialize(root.left)},{serialize(root.right)}$"                
        return serialize(subRoot) in serialize(root)

    # Best memory complexity solution (17.1MB)
    def isSubtreeBestMemory(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def ser(n):
            if not n:
                return ',#'
            return ',' + str(n.val) + ser(n.left) + ser(n.right)
        return ser(subRoot) in ser(root)


if __name__ == "__main__":
    s = Solution()

    rt = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    srt = TreeNode(4, TreeNode(1), TreeNode(2))

    print(s.isSubtree(rt, srt)) # True

    rt = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
    srt = TreeNode(4, TreeNode(1), TreeNode(2))
    print(s.isSubtree(rt, srt)) # False
