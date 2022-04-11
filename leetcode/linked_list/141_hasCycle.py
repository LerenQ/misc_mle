class ListNode:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None
    
class Solution:
    def hasCycle(self, head) -> bool:
        '''
        Given head, the head of a linked list, 
        determine if the linked list has a cycle in it.
        There is a cycle in a linked list 
        if there is some node in the list that 
        can be reached again by continuously following the next pointer. 
        Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
        Note that pos is not passed as a parameter.

        Return true if there is a cycle in the linked list. Otherwise, return false.

        '''
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True

        return False


test = Solution()
a = [8, 3, 2]
l1 = ListNode(a[0])
l1.next = ListNode(a[1])
l1.next.next = ListNode(a[2])
b = [9, 2, 1]
l2 = ListNode(b[0])
l2.next = ListNode(b[1])
l2.next.next = ListNode(b[2])
ans = test.hasCycle(l1)
print(ans)