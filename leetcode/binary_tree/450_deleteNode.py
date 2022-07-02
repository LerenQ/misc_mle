# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root, key: int):
        '''
        Given a root node reference of a BST and a key, 
        delete the node with the given key in the BST. 
        Return the root node reference (possibly updated) of the BST.
        '''
        if not root: return 
        if root.val == key: 
            if not root.right: return root.left
            if not root.left: return root.right
            if root.right and root.left:
                t_node = self.travRight(root.left)
                t_node.right = root.right  
                root = root.left
            else:
                root = None
      
        if root and root.val > key: root.left = self.deleteNode(root.left, key)     
        if root and root.val < key: root.right = self.deleteNode(root.right, key)
            
        return root
    
    def travRight(self,node):
        if node.right:
            node = self.travRight(node.right)
        return node
        
