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
        collect = {}

        l1 = l2 = head
        while l1:
            collect[l1] = Node(l1.val)
            l1 = l1.next
        while l2:
            collect[l2].next = collect.get(l2.next)
            collect[l2].random = collect.get(l2.random)
            l2 = l2.next
        return collect.get(head)


test = Solution()
a = [8, 3, 2]
l1 = Node(a[0])
l1.next = Node(a[1])
l1.next.next = Node(a[2])
ans = test.copyRandomList(l1)
print(ans)