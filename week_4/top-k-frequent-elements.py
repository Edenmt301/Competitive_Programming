class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency={}
        answers=[]
        for i in nums:
            if i in frequency:
                frequency[i]+=1
            else:
                frequency[i]=1
        print(frequency)
        myHeap=[]
        for key in frequency:
            heapq.heappush(myHeap,[-frequency[key],key])
        for i in range(k):
            answers.append(heapq.heappop(myHeap)[1])
        return answers
