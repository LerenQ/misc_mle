from collections import heapq
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        '''
        Given the root of a binary tree, invert the tree, and return its root.
        '''
        def traverse(node):
            
            if node:
                node_new = TreeNode(node.val)
            else:
                return
            
            if node.left:
                node_new.right = traverse(node.left)
            
            if node.right:
                node_new.left = traverse(node.right)
            
            return node_new
            
        return traverse(root)