class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
    
        vals=[]
        for i in range(n+1):
            if i==0 or i==1 or i==2:
                if i==0:
                    vals.append(0)
                else:
                    vals.append(1)
                continue
            else:
                val=vals[i-1] + vals[i-2] + vals[i-3]
                vals.append(val)
        return vals[-1]  
