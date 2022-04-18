# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given two integer arrays inorder and postorder 
    where inorder is the inorder traversal of a binary tree and 
    postorder is the postorder traversal of the same tree, 
    construct and return the binary tree.

    """
    def buildTree(self, inorder: list, postorder: list):
        
        if postorder == []:
            return None
        ans = TreeNode(postorder[-1])
        ind = inorder.index(postorder[-1])

        ans.left = self.buildTree(inorder[:ind], postorder[:ind])
        ans.right = self.buildTree(inorder[ind+1:], postorder[ind:-1])
        
        return ans
    

test = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
ans = test.buildTree(preorder, inorder)
print(ans)