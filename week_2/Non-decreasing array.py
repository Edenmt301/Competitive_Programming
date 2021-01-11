nums=[4,2,1]
class Solution(object):
    def checkPossibility(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        prev=nums[0]
        for i in range(len(nums)):
            if i<len(nums)-1:
                if prev>nums[i] and nums[i+1]<prev:
                    nums.pop(i-1)
                    break
                if prev>nums[i] and nums[i+1]>=prev:
                    nums.pop(i)
                    break
            else:
                if prev>nums[i]:
                    nums.pop(i)
                    break
            prev=nums[i]
        pre_nums=[i for i in nums]
        nums.sort()
        if pre_nums==nums:
            return True
        else:
            return False
        
print(Solution.checkPossibility(nums))
