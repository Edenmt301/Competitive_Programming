#Triangle 2
rows=int(input())
for i in range(1,rows+1):
    for j in range (rows-i):
        print(' ',end='')
    print(((i*2)-1)*"*")
