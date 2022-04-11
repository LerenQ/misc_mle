# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        '''
        You are given an array of k linked-lists lists, 
        each linked-list is sorted in ascending order.

        Merge all the linked-lists into one sorted linked-list and return it.
        '''
        l = []
        for tmp in lists:
            while tmp:
                l.append(tmp.val)
                tmp = tmp.next
        cur = head = ListNode(0)
        for i in sorted(l):
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
l = [l1, l2]
ans = test.mergeKLists(l)
print(ans.val, ans.next.val, ans.next.next.val)