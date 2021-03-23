class Solution:
    def numDecodings(self, s: str) -> int:
        memo={}
        return self.dfs(s[0], 1, s, memo)+ self.dfs(s[:2], 2, s, memo)
        
    def dfs(self, curr, next_idx, full_string, memo) -> int:
        
        if curr == '0' or int(curr) > 26 or next_idx > len(full_string):
            return 0
        if curr[0] == '0' and len(curr) == 2:
            return 0
        
        if next_idx == len(full_string):
            return 1
        
        if next_idx in memo:
            return memo[next_idx]
        
        p1 = self.dfs(full_string[next_idx], next_idx + 1, full_string, memo)
        memo
        
        p2 = self.dfs(full_string[next_idx: next_idx + 2], next_idx + 2, full_string, memo)
        
        memo[next_idx] = p1 + p2
        return p1 + p2
