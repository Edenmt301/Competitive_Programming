target=int(input())
nums=list(map(int, input().rstrip().split()))
def finder(target,nums):
    valid=True
    for c in nums:
        if c < (-10)**9 or c >(10)**9:
            valid=False
            break
    if len(nums)< 2 or len(nums)>10**3 or target<(-10)**9 or target >(10)**9 or valid==False:
        return('invalid input')
    for i in range(len(nums)):
        found=False
        for j in range(len(nums)):
            if nums[i] + nums[j]==target and i!=j:
                found=True
                return('[' + str(i) + ',' + str(j) + ']')
print(finder(target,nums))        
