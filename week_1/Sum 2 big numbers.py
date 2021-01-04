#addition
a=str(10**1000000)
b=str(10**1000000)
carry=0
answer=''
if len(a)<len(b):
        diff=len(b)-len(a)
        zeros='0'*diff
        a=zeros + a
elif len(b)<len(a):
        diff=len(a)-len(b)
        zeros='0'*diff
        b=zeros + b
i = len(a) - 1
while i>=0:
        c=int(a[i]) + int(b[i])+ carry
        if c>9:
            answer=str(c%10) + answer
            c = c//10
            carry=c
        else:
            answer=str(c) + answer
            carry=0
        i-=1
answer=str(carry) + answer
print(int(answer))
