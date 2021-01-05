array=input().split()

def bubbleSort(array):
    x=len(array)-1
    while x>=0:
        for i in range(x):
            if int(array[i])>int(array[i+1]):
                array[i],array[i+1]=array[i+1],array[i]
        x-=1
    return(array)
print(bubbleSort(array))               








                                                            
































           

































   
