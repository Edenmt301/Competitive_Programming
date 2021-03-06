class MedianFinder:

    def __init__(self):
        self.smallerHalf = []
        self. biggerHalf = []
        """
        initialize your data structure here.
        """
        

    def addNum(self, num: int) -> None:
        if not self.smallerHalf:
            heapq.heappush(self.smallerHalf,-num)
        elif not self.biggerHalf:
            if -self.smallerHalf[0] > num:
                heapq.heappush(self.biggerHalf,-(heapq.heappop(self.smallerHalf)))
                heapq.heappush(self.smallerHalf,-num)
            else:
                heapq.heappush(self.biggerHalf,num)
        else:
            if len(self.smallerHalf) == len(self.biggerHalf):
                if -self.smallerHalf[0] >= num or self.biggerHalf[0] > num:
                    heapq.heappush(self.smallerHalf,-num)
                else:
                    heapq.heappush(self.smallerHalf,-(heapq.heappop(self.biggerHalf)))
                    heapq.heappush(self.biggerHalf,num)
            elif len(self.smallerHalf) > len(self.biggerHalf):
                if num < -self.smallerHalf[0]:
                    heapq.heappush(self.biggerHalf,-(heapq.heappop(self.smallerHalf)))
                    heapq.heappush(self.smallerHalf,-num)
                else:
                    heapq.heappush(self.biggerHalf,num)
    def findMedian(self) -> float:
        if not self.smallerHalf:
            return 0
        if len(self.smallerHalf) == len(self.biggerHalf):
            return ((-self.smallerHalf[0]) + self.biggerHalf[0])/2
        else:
            return -self.smallerHalf[0]
