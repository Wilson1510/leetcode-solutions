"""
Complexity:
- Time  : O(n)
- Space : O(n)
"""
from typing import Optional, List


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
    # Runtime: 4ms
    # Memory Usage: 20.2MB
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
    
        root = TreeNode(preorder[0])
        stack = [root]
        inorder_ptr = 0
        
        for i in range(1, len(preorder)):
            curr_val = preorder[i]
            node = stack[-1]

            if node.val != inorder[inorder_ptr]:
                node.left = TreeNode(curr_val)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorder_ptr]:
                    node = stack.pop()
                    inorder_ptr += 1

                node.right = TreeNode(curr_val)
                stack.append(node.right)
                
        return root

    # Best time complexity solution (1ms)
    def buildTreeBestTime(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val:idx for idx,val in enumerate(inorder)}

        self.pre_idx = 0

        def dfs(l,r):
            if l>r:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = indices[root_val]
            root.left = dfs(l,mid-1)
            root.right = dfs(mid+1,r)
            return root

        return dfs(0,len(inorder)-1)

    # Best memory complexity solution (18.16MB)
    def buildTreeBestMemory(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        i, j = 0, 0 # preorder, inorder index
        p = TreeNode(None)
        while i < len(preorder) or j < len(inorder):
            # Build left until inorder & preorder point to same value
            while p.val != inorder[j]:
                # Link each node's right to it's parent
                p.left = TreeNode(preorder[i], None, p)
                p = p.left
                i += 1
            j += 1
            
            # Reached left end; need to find node to build right
            # While the next node inorder == p's parent (right pointer)
                # Move to parent; break link between child & parent
            
            # The p where it's parent isn't next in the inorder is where to
            # build the right tree
            while j < len(inorder) and p.right.val == inorder[j]:
                p.right, p = None, p.right
                j += 1
            
            if j < len(inorder):
                # If not all nodes have been built
                # Add next node in preorder to the right of p
                p.right = TreeNode(preorder[i], None, p.right)
                p = p.right
                i += 1
            else:
                # p.right is the dummy node
                # move right to dummy & break link to dummy
                p.right, p = None, p.right
        
        return p.left # actual root is left of dummy


if __name__ == "__main__":
    s = Solution()

    print(s.buildTree([3,9,20,15,7], [9,3,15,20,7])) # TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(s.buildTree([-1], [-1])) # TreeNode(-1)
