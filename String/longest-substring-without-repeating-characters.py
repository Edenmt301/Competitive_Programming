class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left=right = 0
        current = set()
        while right < len(s) and left < len(s):
            if s[right] not in current:
                current.add(s[right])
                right += 1
                longest=max(longest, len(current))
            else:
                current.remove(s[left])
                left += 1
            
        return longest
