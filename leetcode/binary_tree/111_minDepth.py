# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given a binary tree, find its minimum depth.
    The minimum depth is the number of nodes 
    along the shortest path from the root node down to the nearest leaf node.
    Note: A leaf is a node with no children.

    """
    def minDepth(self, root) -> int:

        if not (root.left or root.right):
            return 0
        if root:
            
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
    

test = Solution()
a = [1,3,2,3]
root = TreeNode(a[0])
root.left = TreeNode(a[1])
root.right = TreeNode(a[2])
root.right.left = TreeNode(a[3])
ans = test.minDepth(root)
print(ans)