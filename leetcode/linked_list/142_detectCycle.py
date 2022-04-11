class ListNode:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None
    
class Solution:
    def detectCycle(self, head):
        '''
        Given the head of a linked list, 
        return the node where the cycle begins. 
        If there is no cycle, return null.

        There is a cycle in a linked list if 
        there is some node in the list that can be reached again 
        by continuously following the next pointer. 
        Internally, pos is used to denote the index of the node that 
        tail's next pointer is connected to (0-indexed). 
        It is -1 if there is no cycle. Note that pos is not passed as a parameter.

        Do not modify the linked list.

        '''
        seen = set()
        while head:
            if head in seen:
                return head
            else:
                seen.add(head)
            head = head.next
        return None


test = Solution()
a = [8, 3, 2]
l1 = ListNode(a[0])
l1.next = ListNode(a[1])
l1.next.next = ListNode(a[2])
b = [9, 2, 1]
l2 = ListNode(b[0])
l2.next = ListNode(b[1])
l2.next.next = ListNode(b[2])
ans = test.detectCycle(l1)
print(ans)