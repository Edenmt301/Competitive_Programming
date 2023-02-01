class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
         dp = [0] * len(scores)
        answer = 0
        elements = []
        for i in range(len(scores)):
            elements.append((ages[i], scores[i]))

        elements.sort(key = lambda x: (x[0],x[1]))
        for i in range(len(scores)):
            dp[i] = elements[i][1]
            for j in range(i):
                if elements[j][1] <= elements[i][1]:
                    dp[i] = max( dp[j] + elements[i][1], dp[i])
            ans = max(answer, dp[i])
        return ans
