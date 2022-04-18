# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given two integer arrays preorder and inorder 
    where preorder is the preorder traversal of a binary tree and 
    inorder is the inorder traversal of the same tree, 
    construct and return the binary tree.

    """
    def buildTree(self, preorder, inorder: list):
        
        if preorder == []:
            return None
        root_val = preorder[0]
        ans = TreeNode(root_val)
        ind = inorder.index(root_val)

        ans.left = self.buildTree(preorder[1:ind+1],inorder[:ind])
        ans.right = self.buildTree(preorder[ind+1:],inorder[ind+1:])
        
        return ans
    

test = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
ans = test.buildTree(preorder, inorder)
print(ans)