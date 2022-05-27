from collections import heapq
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):
        '''
        Given the root of a binary tree, determine if it is a valid binary search tree (BST).
        '''
        b, _, _  = self.traverse(root)
        return b
        
    def traverse(self, node):
        lb = rb = True
        minv = maxv = node.val
        if node.left:
            l, v1, v2 = self.traverse(node.left) 
            lb = l & (v2 < node.val)
            minv = v1

        if node.right:
            r, v1, v2 = self.traverse(node.right) 
            rb = r & (v1 > node.val)
            maxv = v2

        return lb&rb, minv, maxv