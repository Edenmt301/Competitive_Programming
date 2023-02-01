class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        n = len(scores)
        dp = [0] * n
        ans = 0
        players = [(ages[i], scores[i]) for i in range(n)]
        players.sort(key = lambda x: (x[0],x[1]))
        for i in range(n):
            dp[i] = players[i][1]
            for j in range(i):
                if players[j][1] <= players[i][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])
            ans = max(ans, dp[i])
        return ans