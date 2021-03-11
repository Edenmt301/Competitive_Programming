class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency={}
        answers=[]
        for i in words:
            if i in frequency:
                frequency[i]+=1
            else:
                frequency[i]=1
        myHeap=[]
        for key in frequency:
            heapq.heappush(myHeap,[-frequency[key],key])
        for i in range(k):
            answers.append(heapq.heappop(myHeap)[1])
        return answers
