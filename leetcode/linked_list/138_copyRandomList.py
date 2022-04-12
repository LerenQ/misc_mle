# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        '''
        A linked list of length n is given such that 
        each node contains an additional random pointer,
        which could point to any node in the list, or null.
        None of the pointers in the new list should point to nodes in the original list.

        '''
        l = head
        while head:
            l.next = head.next
            l = l.next


test = Solution()
a = [8, 3, 2]
l1 = Node(a[0])
l1.next = Node(a[1])
l1.next.next = Node(a[2])
ans = test.copyRandomList(l1)
print(ans)