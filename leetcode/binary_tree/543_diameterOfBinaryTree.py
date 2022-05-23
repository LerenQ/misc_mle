from collections import heapq
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        '''
        Given the root of a binary tree, return the length of the diameter of the tree.
        '''
        rst = []
        
        def traverse(node):
            l = r = 0
            if node.left:
                l = traverse(node.left) + 1
            if node.right:
                r = traverse(node.right) + 1
            
            heapq.heappush(rst, -(l+r))
            return max(l, r)
        
        traverse(root)
        return -rst[0]