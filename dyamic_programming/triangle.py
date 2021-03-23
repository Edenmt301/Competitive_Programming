class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row=len(triangle)-1
        memo={}
        start=(0,0)
        return self.findMin(start, memo, triangle, row)
    
    def findMin(self, curr, memo, triangle, row):
        directions=((1,0),(1,1))
        if curr[0]==row:
            return triangle[curr[0]][curr[1]]
        
        first=curr[0]+directions[0][0],curr[1]+directions[0][1]
        second=curr[0]+directions[1][0],curr[1]+directions[1][1]
        
        if first in memo:
            r1=memo[first]
        else:
            r1=self.findMin(first, memo, triangle, row)
            memo[first]=r1
            
        if second in memo:
            r2=memo[second]
        else:
            r2=self.findMin(second, memo, triangle, row)
            memo[second]=r2
       
        return triangle[curr[0]][curr[1]] + min(r1,r2)
    
            
