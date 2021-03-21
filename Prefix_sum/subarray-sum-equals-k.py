class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count={}
        summ=0
        total=0
        
        for i in nums:
            if summ in count:
                count[summ]+=1
            else:
                count[summ]=1
                
            summ+=i
            if summ-k in count:
                total+=count[summ-k]
                
        return total
