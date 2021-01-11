import math
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        length=len(A)-1
        for i in range (length,1,-1):                      
            perimeter=A[i]+A[i-1]+A[i-2]
            p=perimeter/2
            area=math.ceil(p*(p-A[i])*(p-A[i-1])*(p-A[i-2]))
            if area>0 :
                return perimeter
        return 0
