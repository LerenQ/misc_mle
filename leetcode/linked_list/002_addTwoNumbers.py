# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        '''
        You are given two non-empty linked lists representing two non-negative integers. 
        The digits are stored in reverse order, 
        and each of their nodes contains a single digit. 
        Add the two numbers and return the sum as a linked list.

        You may assume the two numbers do not contain any leading zero, 
        except the number 0 itself.
        '''

        carry = 0
        move = 1
        cur = head = ListNode(0)
        while carry or move:
            if l1.val + l2.val + carry >= 10:
                m = (l1.val + l2.val + carry) % 10
                carry = 1
            else:
                m = (l1.val + l2.val + carry)
                carry = 0
            cur.next = ListNode(m)
            if not (l1.next or l2.next):
                move = 0
            l1 = l1.next if l1.next else ListNode(0)
            l2 = l2.next if l2.next else ListNode(0)           
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
ans = test.addTwoNumbers(l1, l2)
print(ans.val, ans.next.val, ans.next.next.val)