class ListNode:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        '''
        Given the head of a singly linked list, 
        reverse the list, and return the reversed list.

        '''

        l = []
        while head:
            l.append(head.val)
            head = head.next
        cur = head = ListNode(0)
        for i in reversed(l):
            cur.next = ListNode(i)
            cur = cur.next
        return head.next


test = Solution()
a = [8, 3, 2]
l1 = ListNode(a[0])
l1.next = ListNode(a[1])
l1.next.next = ListNode(a[2])
b = [9, 2, 1]
l2 = ListNode(b[0])
l2.next = ListNode(b[1])
l2.next.next = ListNode(b[2])
ans = test.reverseList(l1)
print(ans.val)     