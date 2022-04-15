# Definition for a binary tree node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    """
    Given the root of an n-ary tree, 
    return the postorder traversal of its nodes' values.

    Nary-Tree input serialization is represented in their level order traversal. 
    Each group of children is separated by the null value (See examples)

    """
    def postorder(self, root) -> 'list[int]':
        
        ans = []

        def dfs(node):
            if not node:
                return
            stack = []
            stack.extend(node.children)
            for i in stack:
                dfs(i)
                ans.append(i.val)
                
        dfs(root)
        if root:
            ans.append(root.val)
        
        return ans

test = Solution()
a = [1,None,2,3]
root = Node(a[0])
root.left = Node(a[1])
root.right = Node(a[2])
root.right.left = Node(a[3])
ans = test.preorder(root)
print(ans)