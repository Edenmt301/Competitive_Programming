class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        subtraction = 0
        numOfInts = 0
        nums.sort()
        for num in nums:
            if num > subtraction:
               subtraction = num
               numOfInts += 1
        return numOfInts