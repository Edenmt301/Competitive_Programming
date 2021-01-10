class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        depth=0
        maxim=0
        for i in s:
            if i=='(' :
                depth+=1
                prev='('
            if i==')':
                if depth>maxim:
                    maxim=depth
                depth-=1
                prev=')'
        return maxim
