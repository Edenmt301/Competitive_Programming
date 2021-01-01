#multiplication
a=str(10**1000)
b=str(10**1000)
answer=0
zeros=''
if a<b:
    a,b=b,a
i=len(b)-1
while(i>=0):
    carry=0
    this=''
    for j in range((len(a)-1),-1,-1):
        c=int(a[j])*int(b[i])+carry
        if c>9:
           this=str(c%10) + this
           c = c//10
           carry=str(c)
        else:
            this=str(c) + this
            carry=0
    if i!=len(b)-1:
        zeros +='0'
    answer=answer+int(this+zeros)
    i-=1
print(answer)        




