class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        for i in s:
            occ=1
            if stack and stack[-1][0]==i:
                occ =(stack[-1])[1] + 1
            stack.append([i,occ])
            
         
            if occ==k:
                for j in range(k):
                    stack.pop()
               
        newS=""
        for i in stack:
            newS +=i[0]
        return newS
            
