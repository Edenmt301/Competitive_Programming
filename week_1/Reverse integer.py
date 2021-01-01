x=int(input())
def reverse( x: int) -> int:
        if x <-2**31 or x >(2**31)-1:
            return(0)
        inverted=''
        negative=False
        x=str(x)
        if x[0]=='-':
            negative=True
            x=x.replace('-','')
        for i in x:
            inverted =i + inverted
        inverted=int(inverted)
        if int(inverted) <-2**31 or int(inverted) >(2**31)-1:
            return(0)
        if negative==True:
            inverted ='-' + str(inverted) 
        return(inverted)
print(reverse(x))
