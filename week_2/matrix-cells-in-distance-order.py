class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        cors=[[] for y in range(1000)]
        new=[]
        for i in range(R):
            for j in range(C):
                dis=abs(i - r0) + abs(j - c0)
                cors[dis].append([i,j])
        for j in cors:
            for x in range(len(j)):
                val=j.pop(0)
                new.append(val)
        
      
        return(new)
