# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given the root of a binary tree, return its maximum depth.

    A binary tree's maximum depth is the number of nodes 
    along the longest path from the root node down to the farthest leaf node.

    """
    def maxDepth(self, root) -> int:
        
        def dfs(node, d):
            
            if node.left and node.right:
                return max(dfs(node.left, d + 1), dfs(node.right, d + 1))
            elif node.left:
                return dfs(node.left, d + 1)
            elif node.right:
                return dfs(node.right, d + 1)
            else:
                return d
        
        if root:
            return dfs(root, 1)
        return 0
    

test = Solution()
a = [1,3,2,3]
root = TreeNode(a[0])
root.left = TreeNode(a[1])
root.right = TreeNode(a[2])
root.right.left = TreeNode(a[3])
ans = test.maxDepth(root)
print(ans)