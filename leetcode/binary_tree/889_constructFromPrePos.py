# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given two integer arrays, preorder and postorder 
    where preorder is the preorder traversal of a binary tree of distinct values and 
    postorder is the postorder traversal of the same tree, 
    reconstruct and return the binary tree.

    If there exist multiple answers, you can return any of them.

    """
    def constructFromPrePost(self, preorder: list, postorder: list):
        
        if preorder == []:
            return None
        
        ans = TreeNode(preorder[0])
        pre = preorder[1:]
        post = postorder[:-1]
        ind = 0
        for i in range(len(pre)):
            if sorted(pre[:i+1]) == sorted(post[:i+1]):
                ind = i
                break
        ans.left = self.constructFromPrePost(preorder[1:ind+2], postorder[:ind+1])
        ans.right = self.constructFromPrePost(preorder[ind+2:], postorder[ind+1:-1])

        return ans
    

test = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
ans = test.constructFromPrePost(preorder, inorder)
print(ans)