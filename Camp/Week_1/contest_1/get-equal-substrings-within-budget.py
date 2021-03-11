class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diff = []
        maxCount = 0
        
        for i in range(len(s)):
            x = ord(s[i]) - ord(t[i])
            if x < 0:
                    x *= -1
            diff.append(x)
        
        queue = []
        i = 0
        maxCount=0
        while i < len(diff):
            if diff[i]<=maxCost:
                queue.append(diff[i])
                maxCost-=diff[i]
                maxCount=max(maxCount,len(queue))
            else:
                if queue:
                    x=queue.pop(0)
                    maxCost += x
                    i-=1
            i+=1
        return maxCount     
                
                
                
        
