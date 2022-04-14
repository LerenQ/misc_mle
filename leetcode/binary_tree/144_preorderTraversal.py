# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given the root of a binary tree,
    return the preorder traversal of its nodes' values.
    """
    def preorderTraversal(self, root) -> 'list[int]':
        ans, stack = [], []
        while stack or root:
            while root:
                stack.append(root.right)
                ans.append(root.val)
                root = root.left
            root = stack.pop()
        return ans
            


test = Solution()
a = [1,None,2,3]
root = TreeNode(a[0])
root.left = TreeNode(a[1])
root.right = TreeNode(a[2])
root.right.left = TreeNode(a[3])
ans = test.preorderTraversal(root)
print(ans)