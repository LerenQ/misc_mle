class Solution:
    def numTrees(self, n: int) -> int:
        '''
        Given an integer n, 
        return the number of structurally unique BST's (binary search trees) 
        which has exactly n nodes of unique values from 1 to n.
        
        '''
        self.rec = {0:1, 1:1, 2:2}
        return self.traverse(n)
    
    def traverse(self, n):
        if n in self.rec.keys():
            return self.rec[n]
        else:
            combs = 0
            for i in range(n):
                combs += self.traverse(i) * self.traverse(n-i-1)
                # print(combs)
            self.rec[n] = combs
        return combs
