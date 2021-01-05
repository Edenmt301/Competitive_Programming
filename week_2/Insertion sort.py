array=input().split()

def insertionSort(array):
    for i in range(len(array)):
        x=array[i]
        for j in range(0,i):
            if int(x)<int(array[j]):
                array.pop(i)
                array.insert(j,x)
                break
            elif(i==j):
                array.pop(i)
                array.insert(i+1,x)
                break
    return array
print(insertionSort(array))
