class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]
        suffix=[1]
        answer=[]
        for i in range(len(nums)-1):
            prefix.append(nums[i]*prefix[-1])
            suffix.append((nums[len(nums)-1 -i])*suffix[-1])
        
        for j in range(len(nums)):
            answer.append(prefix[j]*suffix[len(suffix)-1 -j])
            
        return answer
