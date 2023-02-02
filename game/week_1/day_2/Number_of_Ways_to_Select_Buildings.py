class Solution(object):
    def numberOfWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        prefix = [[0,0]]
        suffix = [[0,0]]
        n = len(s)
        for i in range(n - 1):
            num0, num1 =  s[i] == "0" , s[i] == "1"
            prefix.append([prefix[-1][0] + num0, prefix[-1][1] + num1])
            num0, num1 = s[n - i -1] == "0" ,s[n - i -1] == "1" 
            suffix.append([suffix[-1][0] + num0, suffix[-1][1] + num1])
            
        total = 0
        for i in range(n):
            if s[i] == "0":
                total += prefix[i][1] * suffix[n - i - 1][1]
            if s[i] == "1":
                total += prefix[i][0] * suffix[n - i - 1][0]
        return total
