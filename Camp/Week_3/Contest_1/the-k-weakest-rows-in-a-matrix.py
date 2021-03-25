class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap=[]
        answer=[]
        for i in range(len(mat)):
            count=0
            for j in mat[i]:
                if j==1:
                    count+=1
                    continue
                break
            heapq.heappush(heap,(count,i))
        for i in range(k):
            answer.append(heapq.heappop(heap)[1])
        return answer
