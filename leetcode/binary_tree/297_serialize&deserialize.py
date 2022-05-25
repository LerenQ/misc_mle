from collections import heapq
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    ''' this method doesn't work since ingredients may be duplicated'''
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        if not root:
            return 'null'
        
        preorder = []
        inorder = []
        
        def traverse(node, state, action):
            state += action
            preorder.append((node.val, state))
            
            if node.left:
                traverse(node.left, state, 'l')
            inorder.append((node.val, state))
            if node.right:
                traverse(node.right, state, 'r')
        
        traverse(root, '', '')
        ans = ';'.join(str(i) for i in preorder) + '=' + ';'.join(str(i) for i in inorder)
        return ans
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == 'null':
            return
        preorder, inorder = data.split('=')
        preorder = preorder.split(';')
        inorder = inorder.split(';')
        
        def buildTree(preorder, inorder):
            if len(preorder) == 0:
                return
            node = TreeNode(preorder[0].split(',')[0][1:])
            ind = inorder.index(preorder[0])
            
            node.left = buildTree(preorder[1:ind+1], inorder[:ind])
            node.right = buildTree(preorder[ind+1:], inorder[ind+1:])
            
            return node
            
        return buildTree(preorder, inorder)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
