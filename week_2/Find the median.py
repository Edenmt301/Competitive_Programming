def findMedian(arr):
    arr.sort()
    n=len(arr)
    median=arr[n//2]
    return median

n = int(input())
arr = list(map(int, input().rstrip().split()))
result = findMedian(arr)
print(result)
