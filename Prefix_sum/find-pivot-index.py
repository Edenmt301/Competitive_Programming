class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = [0]
        right = [0]
        
        for i in range(len(nums) - 1):
            left.append(nums[i] + left[-1])
            right.append((nums[len(nums) - 1 - i]) + right[-1])
            
        for j in range(len(nums)):
            if(left[j] == right[(len(right) - 1) - j]):
                return j
        return -1
