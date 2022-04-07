class Solution(object):

    def mergeTwoLists(self, l1, l2):
        """
        Merge two sorted linked lists and return it as a sorted list.
        The list should be made by splicing together the nodes of the first two lists.
        """
        new = []
        if len(l1) == 0:
            new = l2
            l2 = []
        elif len(l2) == 0:
            new = l1
            l1 = []
        while len(l1) != 0 and len(l2) != 0:
            # print(new)
            if l1[0] < l2[0]:
                new.append(l1[0])
                l1.pop(0)
            else:
                new.append(l2[0])
                l2.pop(0)
        if len(l1) == 0:
            new += l2
        elif len(l2) == 0:
            new += l1
        return new


test = Solution()
l1 = [1, 2, 4]
l2 = [1, 3, 4]
p = test.mergeTwoLists(l1, l2)
print(p)
