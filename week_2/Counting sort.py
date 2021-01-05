import random
#array=input().split()
array=[random.randint(1, 1000) for i in range(100)]
def countingSort(array):
    correct=[]
    maximum=int(max(array))
    counts=[0 for i in range(maximum+1)]
    for j in array:
        counts[int(j)]+=1
    for x in range(len(counts)):
        correct.extend([int(x)for i in range(counts[x])])
    return correct
print(countingSort(array))        
