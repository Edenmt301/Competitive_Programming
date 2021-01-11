class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev=''
        i=0
        length=len(nums)
        while i<len(nums):
            if prev==nums[i]:
                nums.pop(i)
                i-=1
            else:
                prev=nums[i]
            i+=1
        
        return len(nums)
