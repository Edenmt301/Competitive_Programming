class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left=1
        right=n
        mid=n//2
        while(left<=right):
            print(mid)
            if isBadVersion(mid)==False:
                left=mid+1
            elif isBadVersion(mid)==True:
                if isBadVersion(mid-1)==False or mid==1:
                    return mid
                right=mid-1
            mid=((right+left)//2)
