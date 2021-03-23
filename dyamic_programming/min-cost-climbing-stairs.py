class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo={}
        for i in range(len(cost)-1, -1, -1):
            if i==len(cost)-1 or i==len(cost)-2:
                memo[i]=cost[i]
                continue
            memo[i]=cost[i] + min(memo[i+1],memo[i+2])
        return min(memo[0],memo[1])
            
