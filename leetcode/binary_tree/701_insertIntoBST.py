# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root, val: int):
        '''
        You are given the root node of a binary search tree (BST) and a value to insert into the tree. 
        Return the root node of the BST after the insertion. 
        It is guaranteed that the new value does not exist in the original BST.
        '''

        if not root: return TreeNode(val)
        if root.val > val: root.left = self.insertIntoBST(root.left, val)
        if root.val < val: root.right = self.insertIntoBST(root.right, val)
                
        return root

