from collections import heapq
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root, k: int) -> int:
        '''
        Given the root of a binary search tree, and an integer k, 
        return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
        '''
        rst = []
        
        def traverse(node):
            
            heapq.heappush(rst, node.val)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            
        traverse(root)
        
        cnt = 1
        while cnt < k:
            heapq.heappop(rst)
            cnt += 1
        return rst[0]
