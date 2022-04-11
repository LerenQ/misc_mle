# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        '''
        You are given the heads of two sorted linked lists list1 and list2.
        Merge the two lists in a one sorted list.
        The list should be made by splicing together the nodes of the first two lists.

        Return the head of the merged linked list.
        '''

        cur = head = ListNode(0)
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2

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
ans = test.mergeTwoLists(l1, l2)
print(ans.val, ans.next.val, ans.next.next.val)