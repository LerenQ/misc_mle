class Solution(object):

    def plusOne(self, digits):
        """
        You are given a large integer represented as an integer array digits,
        where each digits[i] is the ith digit of the integer.
        The digits are ordered from most significant to least significant
        in left-to-right order. The large integer does not contain any leading 0's.
        Increment the large integer by one and return the resulting array of digits.
        """
        increase = 1
        for i in reversed(range(len(digits))):
            # print(i)
            if increase:
                if digits[i] == 9 and i != 0:
                    digits[i] = 0
                elif digits[i] == 9 and i == 0:
                    digits[i] = 0
                    digits.insert(0, 1)
                else:
                    digits[i] += 1
                    increase = 0
            else:
                break
        return digits
    
    def plusOne2(self, digits: 'list[int]') -> 'list[int]':
        num = int(''.join(map(str, digits)))
        return [int(d) for d in str(num + 1)]


test = Solution()
digits = [1, 2, 3]
digits = [4, 3, 2, 1]
digits = [0]
digits = [9]
digits = [9, 9, 9]
digits = [8, 7, 9]
p = test.plusOne(digits)
print(p)
