class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new=nums
        if len(nums)>1:
            mid=len(nums)//2
            left=nums[0:mid]
            right=nums[mid:len(nums)]
            self.sortArray(left)
            self.sortArray(right)
            left_i=0
            right_i=0
            main_i=0
            while left_i<len(left) and right_i<len(right):
                if left[left_i]<right[right_i]:
                    new[main_i]=left[left_i]
                    left_i+=1
                    main_i+=1
                else:
                    new[main_i]=right[right_i]
                    right_i+=1
                    main_i+=1
            if left_i<len(left):
                while left_i<len(left):
                    new[main_i]=left[left_i]
                    left_i+=1
                    main_i+=1
            if right_i<len(right):
                while right_i<len(right):
                    new[main_i]=right[right_i]
                    right_i+=1
                    main_i+=1
        return new
