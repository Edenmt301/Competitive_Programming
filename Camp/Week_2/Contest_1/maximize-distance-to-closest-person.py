class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        dis=0
        i=0
        while(i<len(seats)):
            count=0
            while (i + count)<len(seats) and (seats[i + count]==0):
                count+=1
                
            if (i + count-1 == len(seats) - 1) or (i==0 and seats[i]==0):
                dis=max(dis,count)
                i+=count + 1
                continue
        
            dis=max(dis, (count // 2) + (count % 2))
            i+=count + 1
           
        return dis
            
