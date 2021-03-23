class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        max_sum=0
        heapq.heapify(A)

        for i in range(K):
            heapq.heappush(A, -heapq.heappop(A))
            
        for x in A:
            max_sum+=x
            
        return max_sum
