class ListNode:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val: int):
        '''
        Given the head of a linked list and an integer val, 
        remove all the nodes of the linked list that has Node.val == val, 
        and return the new head.

        '''
        ans = l = ListNode(0)
        l.next = head
        while l.next:
            if l.next.val == val:
                l.next = l.next.next
            else:
                l = l.next
        return ans.next


test = Solution()
a = [4, 5, 6]
l1 = ListNode(a[0])
l1.next = ListNode(a[1])
l1.next.next = ListNode(a[2])
ans = test.removeElements(l1, 6)
print(ans.next.next.val)     