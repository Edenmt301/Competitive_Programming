def matchingStrings(strings, queries):
    result=[]
    for i in queries:
        count=0
        l=len(strings)
        j=0
        while j<l:
            if i==strings[j]:
                count +=1
            j+=1
        result.append(count)
    return result
