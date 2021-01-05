n=int(input("enter the number of socks:"))
ar=input("enter the sock colors:")
ar=ar.split()
for i in range(len(ar)):
        ar[i]=int(ar[i])
def socks(n,ar):
    count=0
    valid=True
    for i in ar:
        if i<1 or i>100:
            valid=False
            break
    if n<0 or n>100 or len(ar)!=n or valid==False:
        print("invalid input")
        return()
    for i in range(len(ar)):
        sock=ar.pop(0)
        for j in range(len(ar)):
            if ar[j]== sock:
                count +=1
                ar.pop(j)
                break
        if len(ar)==0:
            break
    return count
print(socks(n,ar))
