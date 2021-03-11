class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        move = 0
        A.sort()
        for i in range(len(A)):
            if i-1 >= 0 and A[i-1] == A[i]:
                move+=1
                A[i]+=1
            elif  i-1 > 0 and A[i-1] > A[i]:
                move +=  A[i-1] - A[i] + 1
                A[i] =  A[i-1] + 1
        return move
