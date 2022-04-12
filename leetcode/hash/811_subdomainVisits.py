class Solution:
    def subdomainVisits(self, cpdomains: 'list[str]') -> 'list[str]':
        '''
        A website domain "discuss.leetcode.com" consists of various subdomains. 
        At the top level, we have "com", at the next level, 
        we have "leetcode.com" and at the lowest level, 
        "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", 
        we will also visit the parent domains "leetcode.com" and "com" implicitly.

        A count-paired domain is a domain that has one of the two formats "rep d1.d2.d3" 
        or "rep d1.d2" where rep is the number of visits to the domain and d1.d2.d3 is the domain itself.

        For example, "9001 discuss.leetcode.com" is a count-paired domain that indicates that discuss.
        leetcode.com was visited 9001 times.
        Given an array of count-paired domains cpdomains, 
        return an array of the count-paired domains of each subdomain in the input. 
        You may return the answer in any order.
        
        '''
        cpdic = dict()
        ans = []
        for domain in cpdomains:
            num, dom = domain.split(' ')
            sec = dom.split('.')
            dlst = []
            for i in range(len(sec)):
                dlst.append('.'.join(j for j in sec[i:]))
            for i in dlst:
                cpdic[i] = int(num) + cpdic[i] if cpdic.get(i) else int(num)

        for k, v in cpdic.items():
            ans.append(' '.join([str(v), k]))
        
        return ans

    
test = Solution()
cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
ans = test.subdomainVisits(cpdomains)
print(ans)