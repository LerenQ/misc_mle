class ListNode:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head, left, right):
        '''
        Given the head of a singly linked list and two integers left and right 
        where left <= right, 
        reverse the nodes of the list from position left to position right, 
        and return the reversed list.

        '''

        l = []
        while head:
            l.append(head.val)
            head = head.next
        l = l[0:left-1] + [i for i in reversed(l[left-1:right])] +l[right:]
        cur = head = ListNode(0)
        for i in l:
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
ans = test.reverseList(l1, 1, 1)
print(ans.val)     