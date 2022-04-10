# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        '''
        You are given two non-empty linked lists representing two non-negative integers. 
        The most significant digit comes first and each of their nodes contains a single digit. 
        Add the two numbers and return the sum as a linked list.

        You may assume the two numbers do not contain any leading zero, except the number 0 itself.
        '''

        v1 = v2 = 0
        while l1:
            v1 = v1 * 10 + l1.val
            l1 = l1.next
        while  l2:
            v2 = v2 * 10 + l2.val
            l2 = l2.next
        v = v1 + v2
        print(v)
        cur = head = ListNode(0)
        for i in str(v):
            cur.next = ListNode(int(i))
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
ans = test.addTwoNumbers(l1, l2)
print(ans.val, ans.next.val, ans.next.next.val)