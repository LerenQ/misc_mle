# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given the root of a binary tree, 
    check whether it is a mirror of itself (i.e., symmetric around its center).

    """
    def isSymmetric(self, root) -> bool:
        
        def isSame(l, r):
            if l and r:
                return (isSame(l.right, r.left) and isSame(l.left, r.right) and (l.val == r.val))
            else:
                return l is r

        l = root.left
        r = root.right

        if l and r:
            return isSame(l, r)
        else:
            return l is r
    

test = Solution()
a = [1,3,2,3]
root = TreeNode(a[0])
root.left = TreeNode(a[1])
root.right = TreeNode(a[2])
root.right.left = TreeNode(a[3])
ans = test.isSymmetric(root)
print(ans)