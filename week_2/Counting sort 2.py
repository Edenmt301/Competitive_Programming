#array=list(map(int, input().rstrip().split()))
import random
array=[random.randint(-100,100) for i in range(100)]

def countingSort(array):
    correct=[]
    minimum=int(min(array))
    maximum=int(max(array))    
    shift=0
    if minimum>=0:
        counts=[0 for i in range(maximum+1)]
    else:
        counts=[0 for i in range(maximum-minimum+1)]
        shift=-1*minimum
    for j in array:
            counts[int(j)+shift]+=1
    for x in range(len(counts)):
        correct.extend([(int(x)-shift)for i in range(counts[x])])
    return correct
print(countingSort(array))
