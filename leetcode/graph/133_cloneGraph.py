
# Definition for a Node.
from collections import defaultdict

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        '''
        Given a reference of a node in a connected undirected graph.
        Return a deep copy (clone) of the graph.
        Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

        '''
        
        ans = defaultdict(lambda: Node(0,[]))
        col = set()
        q = {node}

        while q:
            n = q.pop()
            if n:
                ans[n.val].val = n.val
                for i in n.neighbors:
                    ans[n.val].neighbors.append(ans[i.val])
                    if i not in col:
                        q.add(i)
            col.add(n)
            
        return ans[node.val] if node else node
