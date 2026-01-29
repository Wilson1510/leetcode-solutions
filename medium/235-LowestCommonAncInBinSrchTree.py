"""
Complexity:
- Time  : O(h) h is height of tree
- Space : O(h)
"""


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
    # Runtime: 55ms
    # Memory Usage: 23.04MB
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

    # Best time complexity solution (34ms)
    def lowestCommonAncestorBestTime(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if (p.val <= root.val and q.val >= root.val) or (p.val >= root.val and q.val <= root.val):
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

    # Best memory complexity solution (19.3MB)
    def lowestCommonAncestorBestMemory(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root == None or root == p or root == q: return root
        root.left = self.lowestCommonAncestor(root.left, p, q)
        root.right = self.lowestCommonAncestor(root.right, p, q)
        if root.left != None and root.right != None: return root
        if root.left != None: return root.left
        return root.right


if __name__ == "__main__":
    s = Solution()

    r = TreeNode(
        6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))),
        TreeNode(8, TreeNode(7), TreeNode(9))
    )

    print(s.lowestCommonAncestor(r, TreeNode(2), TreeNode(8))) # 6
    print(s.lowestCommonAncestor(r, TreeNode(2), TreeNode(4))) # 2
    print(s.lowestCommonAncestor(TreeNode(2, TreeNode(1)), TreeNode(2), TreeNode(1))) # 2
