# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given the roots of two binary trees p and q, 
    write a function to check if they are the same or not.
    Two binary trees are considered the same if they are structurally identical, 
    and the nodes have the same value.

    """
    def isSameTree(self, p, q) -> bool:
        
        def sameNode(nodep, nodeq):
            if nodep.val != nodeq.val:
                return False
            l = sameNode(nodep.left, nodeq.left)
            r = sameNode(nodep.right, nodeq.right)
            if not (l and r):
                return False
            return True
        
        sameNode(p, q)
        
        return True

test = Solution()
a = [1,None,2,3]
root = TreeNode(a[0])
root.left = TreeNode(a[1])
root.right = TreeNode(a[2])
root.right.left = TreeNode(a[3])
ans = test.inorderTraversal(root)
print(ans)