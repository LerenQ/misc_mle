from collections import heapq
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: 'list[int]'):
        m = max(nums)
        ind = nums.index(m)
        
        node = TreeNode(m)
        
        if ind > 0:
            node.left = self.constructMaximumBinaryTree(nums[:ind])
        if len(nums) > ind + 1:
            node.right = self.constructMaximumBinaryTree(nums[ind+1:])
             
        return node
