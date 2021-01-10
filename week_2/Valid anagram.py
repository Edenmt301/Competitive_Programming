class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        
        """
        s=sorted(s)
        t=sorted(t)
        if s==t:
            return True
        else:
            return False
