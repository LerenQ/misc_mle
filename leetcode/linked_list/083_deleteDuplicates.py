class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printLL(self):
        current = head
        printlist = []
        while current:
            printlist.append(current.val)
            current = current.next
        print(printlist)


class Solution(object):
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Given the head of a sorted linked list,
        delete all duplicates such that each element appears only once.
        Return the linked list sorted as well.
        """
        if head is None:
            return head
        current = head.next
        prev = head
        while current is not None:
            if current.val == prev.val:
                prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next
        return head


test = Solution()
a = [1, 1, 2]
a = [1, 2, 2, 3, 3]
head = ListNode(a[0])
head.next = ListNode(a[1])
head.next.next = ListNode(a[2])
head.next.next.next = ListNode(a[3])
head.next.next.next.next = ListNode(a[4])
p = test.deleteDuplicates(head)
p.printLL()
