class Solution:
    def makeConnected(self, n: int, connections: 'list[list[int]]') -> int:
        '''
        There are n computers numbered from 0 to n - 1 connected by ethernet cables connections 
        forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. 
        Any computer can reach any other computer directly or indirectly through the network.

        You are given an initial computer network connections. 
        You can extract certain cables between two directly connected computers, 
        and place them between any pair of disconnected computers to make them directly connected.

        Return the minimum number of times you need to do this in order to make all the computers connected. 
        If it is not possible, return -1.

        '''

        if n - 1 > len(connections):
            return -1
        
        uf = list(range(n))
        
        def union(x, y):
            uf[find(x)] = find(y)
            
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        for u, v in connections:
            union(u, v)
            
        return len({find(i) for i in range(n)}) -1
        
