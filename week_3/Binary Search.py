class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        mid=(right+left)//2
        while(left<=right):
            print(left,right,mid)
          
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                left=mid+1
            if nums[mid]>target:
                right=mid-1
            mid=((right+left)//2)
        return -1
