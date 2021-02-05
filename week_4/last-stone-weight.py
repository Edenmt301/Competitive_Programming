class Solution:
    def lastStoneWeight(self,stones):
        myHeap=[]
        for one in stones:
            heapq.heappush(myHeap,-one)
        while len(myHeap)>1:
            first=heapq.heappop(myHeap)
            second=heapq.heappop(myHeap)
            if first!=second:
                heapq.heappush(myHeap,(first-second))
        if myHeap:
            return -heapq.heappop(myHeap)
        return 0
