class Solution:
    
    #Recursive approach
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        fibon=self.fib(n-1)+self.fib(n-2)
        return fibon

    #Iterative approach
    def fib2(self, n: int) -> int:
        res=[]
        for i in range(n+1):
            if i==0 or i==1: 
                res.append(i)
            else:
                res.append(res[i-1] + res[i-2])
        return res[-1]


