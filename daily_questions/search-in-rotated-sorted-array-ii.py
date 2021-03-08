class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums2=set(nums)
        if target in nums2:
            return True
        return False
