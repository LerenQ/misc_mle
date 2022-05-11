import operator

class Solution:
    def equationsPossible(self, equations: 'list[str]') -> bool:
        '''
        You are given an array of strings equations that represent relationships 
        between variables where each string equations[i] is of length 4 and 
        takes one of two different forms: "xi==yi" or "xi!=yi".Here, 
        xi and yi are lowercase letters (not necessarily different) 
        that represent one-letter variable names.

        Return true if it is possible to assign integers to variable names 
        so as to satisfy all the given equations, or false otherwise.


        '''
        equals = []
        equations.sort(key=lambda x:x[1], reverse=True)
        
        for k, (x, j, _, y) in enumerate(equations):
            # print(equals)
            if j == '=':
                for i1, v1 in enumerate(equals):
                    if (x in v1) | (y in v1):
                        equals[i1].update({x,y})
                        for v2 in equals[i1+1:]:
                            if (x in v2) | (y in v2):
                                equals[i1] = equals[i1].union(v2)
                                break
                        break
                else:
                    equals.append({x,y})
            else:
                if x == y:
                    return False
                for i, v in enumerate(equals):
                    if (x in v) and (y in v):
                        return False

        return True


obj = Solution()
equations = ["b==a","a!=b", 'a==z', 'z!=a']
ans = obj.equationsPossible(equations)
print(ans)