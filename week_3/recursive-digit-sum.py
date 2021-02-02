def superDigit(n, k):
    if int(n)<10:
        return n
    sum=0
    for i in n:
        sum+=int(i)
    sum=sum*k
    k=1
    n=str(sum)
    result=superDigit(n, k)
    return result
