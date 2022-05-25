from collections import heapq
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root):
        duplicate_l = []
        pattern = []
        rst = []
        
        def traverse(node):
            
            pat_l = pat_r = ''
            if not node:
                return 'n'
            pat_l = 'l' + traverse(node.left)
            pat_r = 'r' + traverse(node.right)
            
            pat = str(node.val) + pat_l + pat_r
            
            if pat in pattern:
                if pat not in duplicate_l:
                    duplicate_l.append(pat)
                    rst.append(node)
            else:
                pattern.append(pat)
            # print(pat)
            return pat
            
        traverse(root)
        
        return rst
