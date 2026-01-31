"""
Complexity:
- Time  : O(n)
- Space : O(w) w is width of tree
"""
from typing import Optional, List
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
    # Memory Usage: 19.96MB
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root, 0)])
        result = []

        while queue:
            n, depth = queue.popleft()
            if len(result) == depth:
                result.append([])
            result[depth].append(n.val)

            if n.left:
                queue.append((n.left, depth + 1))
            if n.right:
                queue.append((n.right, depth + 1))

        return result


    # Best time complexity solution (0ms)
    def levelOrderBestTime(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = [root]
        res = []

        while q:
            level = []
            for i in range(len(q)):

                cur = q.pop(0)
                level.append(cur.val)

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                    
            res.append(level)
        
        return res

    # Best memory complexity solution (17.4MB)
    def levelOrderBestMemory(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        res = []
        while queue:
            cur_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                cur_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(cur_level)

        return res


if __name__ == "__main__":
    s = Solution()

    print(s.levelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))) # [[3],[9,20],[15,7]]
    print(s.levelOrder(TreeNode(1))) # [[1]]
    print(s.levelOrder(None)) # []
