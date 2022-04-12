class ListNode:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        '''
        Given the heads of two singly linked-lists headA and headB, 
        return the node at which the two lists intersect. 
        If the two linked lists have no intersection at all, return null.

        For example, the following two linked lists begin to intersect at node c1:
        The test cases are generated such that there are no cycles anywhere in the entire linked structure.
        Note that the linked lists must retain their original structure after the function returns.
        '''
        seen = set()
        l = headA
        while l:
            seen.add(l)
            l = l.next
        l = headB
        while l:
            if l in seen:
                return l
            l = l.next
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
ans = test.getIntersectionNode(l1, l2)
print(ans)     