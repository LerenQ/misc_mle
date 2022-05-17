class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        '''
        Given two integers a and b, return any string s such that:
            s has length a + b and contains exactly a 'a' letters, and exactly b 'b' letters,
            The substring 'aaa' does not occur in s, and
            The substring 'bbb' does not occur in s.
        
        '''
        s = ''
        cnt = 0
        cur = None
        while a>0 or b>0:
            # print(a, b, s, cnt)
            if cnt <= 1:
                if a > b:
                    s += 'a'
                    cnt = cnt + 1 if cur == 'a' else 1
                    cur = 'a'
                    a -= 1
                else:
                    s += 'b'
                    cnt = cnt + 1 if cur == 'b' else 1
                    cur = 'b'
                    b -= 1
            else:
                if cur == 'a':
                    s += 'b'
                    b -= 1
                    cur = 'b'
                else:
                    s += 'a'
                    a -= 1
                    cur = 'a'
                cnt = 1
        return s