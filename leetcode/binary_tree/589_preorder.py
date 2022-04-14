# Definition for a binary tree node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    """
    Given the root of an n-ary tree, 
    return the preorder traversal of its nodes' values.
    N ary-Tree input serialization is represented in their level order traversal. 
    Each group of children is separated by the null value (See examples)

    """
    def preorder(self, root) -> 'list[int]':
        ans, stack = [], root and [root]
        while stack:
            root = stack.pop()
            stack.extend(reversed(root.children))
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