class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        maxScore=0
        score=0
        for i in range(len(tokens)):
            if P >= tokens[0]:
                P -= tokens.pop(0)
                score += 1
                maxScore=max(maxScore,score)
            elif score > 0:
                P += tokens.pop(-1)
                score -= 1
            else:
                break
        return maxScore
