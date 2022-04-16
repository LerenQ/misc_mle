# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children


class Solution:
    """
    Given a n-ary tree, find its maximum depth.
    The maximum depth is the number of nodes 
    along the longest path from the root node down to the farthest leaf node.
    N ary-Tree input serialization is represented in their level order traversal, 
    each group of children is separated by the null value (See examples).

    """
    def maxDepth(self, root) -> int:
        
        if not root:
            return 0
        return max(list(map(self.maxDepth, [root.children])) or [0]) + 1
            
    

test = Solution()
a = [1,3,2,3]
root = TreeNode(a[0])
root.children = None
ans = test.maxDepth(root)
print(ans)