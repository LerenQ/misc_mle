# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    def maxPathSum(self, root) -> int:
        
        res, cur = [], 0
        
        def traverse(node):
            
            if not node.left and not node.right:
                return node.val    
            
            l = r = -1001
            
            if node.left:
                l = traverse(node.left)
            
            if node.right:
                r = traverse(node.right)
            # print(l,r, node.val)
            cur = max(l+node.val, r+node.val, node.val)
            
            ans = max(l, r, max(l, 0) + max(r, 0) + node.val)
            res.append(ans)
            return cur
            
            
        traverse(root)
        return max(res) if res!=[] else root.val
