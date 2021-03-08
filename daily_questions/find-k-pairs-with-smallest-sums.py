class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        output = []
        heap = []
        for i in nums1:
            for j in nums2:
                heapq.heappush(heap, [i + j, [i, j] ])
                
        for r in range(k):
            if heap:
                output.append(heapq.heappop(heap)[1])
        return output
