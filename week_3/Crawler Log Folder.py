class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        op=0
        for i in logs:
            if i=='./':
                continue
            elif i=='../':
                if op>0:
                    op-=1
            else:
                op +=1
        return op
