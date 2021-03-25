class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        half=len(arr)/2
        heap=[]
        nums={}
        answer=0
        for i in range(len(arr)):
            if arr[i] in nums:
                nums[arr[i]][0]+=1
                continue
            nums[arr[i]]=[1,arr[i]]
        for j in nums:
            heapq.heappush(heap,(-nums[j][0],nums[j][1]))
        
        while half>0:
            count,num=heapq.heappop(heap)
            half-=-count
            answer +=1
        return answer
