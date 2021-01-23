n=int(input())
ar = list(map(int, input().rstrip().split()))
def quickSort(ar):
    new=[]
    if len(ar)==1:
        each=[ar[0]]
        return each
    pivot=ar[0]
    left=[]
    right=[]
    
    for i in ar:
        if i<pivot:
            left.append(i)
        elif i>pivot:
            right.append(i)
    if left:
        a=quickSort(left)
        new.extend(a)
        if len(a)>1:
            for j in a:
                print(j, end=' ')
            print(" ")
    new.append(pivot) 
    if right:
        b=quickSort(right)
        new.extend(b)
        if len(b)>1:
            for j in b:
                print(j, end=" ")
            print(" ")
    return new

new=quickSort(ar)
for k in new:
        print(k, end=" ") 

