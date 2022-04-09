class Solution(object):

    def addToArrayForm(self, num: 'list[int]', k: 'int') -> 'list[int]':
        '''
        The array-form of an integer num is an array representing its digits in left to right order.
        For example, for num = 1321, the array form is [1,3,2,1].
        Given num, the array-form of an integer, and an integer k, 
        return the array-form of the integer num + k.
        '''
        num = int(''.join(map(str, num)))
        return [int(i) for i in str(num+k)]

test = Solution()
num = [4, 3, 2, 1]
k = 10
ans = test.addToArrayForm(num, k)
print(ans)