class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        i = 0 
        while i < len(nums) - 1 and nums[i] <= nums[i + 1]:
            if nums[i] == target:
                return True
            i += 1
        if i == len(nums) - 1 or target >= nums[i]:
            if nums[i] == target:
                return True
            return False

        left = i + 1
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return True
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return False
            
