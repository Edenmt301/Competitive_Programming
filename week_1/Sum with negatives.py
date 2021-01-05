#addition
a=10**1000
b=-2*(10**1000)

def addition(a,b,bothneg):
    carry=0
    answer=''
    a=str(a)
    b=str(b)
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
    if bothneg==True:
        answer='-' + answer
    return int(answer)
def negAddition(a,b):
    carry=0
    answer=''
    neg=False
    if b<0:
        b,a=a,b
    if a<0:
        a=-1*a
        if a>b:
            neg=True
        else:
            a,b=b,a
        a=str(a)
        b=str(b)
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
            if (int(a[i]) - int(b[i])+ carry>=0):
                c=int(a[i]) - int(b[i])+ carry
                carry=0
            else:
                c=int('1'+a[i]) - int(b[i])+ carry
                carry=-1
            answer=str(c) + answer
            i-=1
    if neg==True:
        answer='-' + answer
    return int(answer)
def choose(a,b):
    bothneg=False
    if a<0 and b<0:
        bothneg=True
        a=a*-1
        b=b*-1
        print(addition(a,b,bothneg))
    elif a<0 or b<0:
        print(negAddition(a,b))
    else:
        print(addition(a,b,bothneg))
choose(a,b)


    
