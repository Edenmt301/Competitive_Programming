class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def valid(left, right, prev):
            if s[left] == s[right]:
                left = left + 1
                right = right - 1
                if right < left:
                    return True
                return valid(left, right, prev)
            
            if not prev:
                return False
            
            first, second = False, False
            if s[left] == s[right - 1]:
                first = valid(left, right - 1, False)
            if s[left + 1] == s[right]:
                second = valid(left + 1, right, False)
            
            return first or second
        return valid(0, len(s) - 1, True)