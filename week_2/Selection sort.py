array=input().split()

def selectionSort(array):
    i=0
    while i<len(array):
        minimum=int(array[i])
        y=i
        for x in range(i+1,len(array)):
            if int(array[x])<minimum:
                minimum=int(array[x])
                y=x
        array[i],array[y]=array[y],array[i]
        i +=1
    return array
print(selectionSort(array))
            
        
