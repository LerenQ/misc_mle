from collections import heapq
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        '''
        You are given a perfect binary tree where all leaves are on the same level, 
        and every parent has two children. The binary tree has the following definition:

        Populate each next pointer to point to its next right node. 
        If there is no next right node, the next pointer should be set to NULL.
        Initially, all next pointers are set to NULL.
        '''

        def traverse(node):
            if not node:
                return 
            
            if node.left or node.right:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
            
            traverse(node.left)
            traverse(node.right)
            
        traverse(root)
        
        return root