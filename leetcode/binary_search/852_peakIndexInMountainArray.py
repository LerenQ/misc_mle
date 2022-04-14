class Solution:
    def peakIndexInMountainArray(self, arr: 'list[int]') -> int:
        '''
        Let's call an array arr a mountain if the following properties hold:
            arr.length >= 3
            There exists some i with 0 < i < arr.length - 1 such that:
                    arr[0] < arr[1] < ... arr[i-1] < arr[i]
                    arr[i] > arr[i+1] > ... > arr[arr.length - 1]
        Given an integer array arr that is guaranteed to be a mountain, 
        return any i 
        such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
        
        '''
        l, r = 0, len(arr) - 1
        m = (l + r) // 2
        while l + 2 < r:
            lm = (l + m) // 2
            rm = (r + m) // 2
            if arr[lm] > arr[m]:
                r, m = m, lm
            elif arr[rm] > arr[m]:
                l, m = m, rm
            else:
                l, r = lm, rm
        return m
        

test = Solution()
arr = [0,1,0]
arr = [0,2,1,0]
arr = [0,10,5,2]
arr = [3,4,5,1]
ans = test.peakIndexInMountainArray(arr)
print(ans)