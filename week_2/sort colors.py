class Solution(object):
    def sortColors(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeros=0
        twos=len(nums)-1
        i=0
        while i<(len(nums)) and i<=twos:
            if nums[i]==0:
                nums[i],nums[zeros]=nums[zeros],nums[i]
                zeros +=1
            elif nums[i]==2:
                nums[i],nums[twos]=nums[twos],nums[i]
                twos -=1
                i-=1
            i+=1 
        return nums
        
nums=[1,2,0]
print(Solution.sortColors(nums))
