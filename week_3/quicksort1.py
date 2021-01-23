def quickSort(arr):
    pivot=arr[0]
    left=[]
    right=[]
    equal=[]
    
    for i in arr:
        if i<pivot:
            left.append(i)
        elif i>pivot:
            right.append(i)
        else:
            equal.append(i)
    left.extend(equal)
    left.extend(right)
    return left
