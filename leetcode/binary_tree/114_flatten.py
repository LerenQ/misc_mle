from collections import heapq
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        def traverse(node):
            
            if not node:
                return
            tail = node
                
            if node.left:
                tail = traverse(node.left)
                
                temp = node.right
                node.right = node.left
                tail.right = temp
                node.left = None
            
            if node.right:  
                tail = traverse(node.right)
                
            return tail
        
        traverse(root)
        