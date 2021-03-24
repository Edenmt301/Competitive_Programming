class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums
        self.myHeap=[]
        self.minHeap=[]
        for i in nums:
            heapq.heappush(self.myHeap,-i)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.myHeap,-val)
        while len(self.minHeap)<self.k:
            heapq.heappush(self.minHeap, -heapq.heappop(self.myHeap))
        if self.myHeap and (-self.myHeap[0]>self.minHeap[0]):
            heapq.heappush(self.minHeap, -heapq.heappop(self.myHeap))
            heapq.heappush(self.myHeap, -heapq.heappop(self.minHeap))
        return self.minHeap[0]    
            
            
            

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
