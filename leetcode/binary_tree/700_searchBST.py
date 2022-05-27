# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root, val: int):
        
        node = None
        if not root: return
        if root.val == val: return root
        if root.val > val: node = self.searchBST(root.left, val)
        if root.val < val: node = self.searchBST(root.right, val)
        
        return node