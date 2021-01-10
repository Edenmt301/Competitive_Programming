
def maximumToys(prices, k):
    sum=0
    count=0
    prices.sort()
    for i in prices:
        if sum+i<k:
            sum +=i
            count+=1
    return count


nk = input().split()

n = int(nk[0])

k = int(nk[1])

prices = list(map(int, input().rstrip().split()))

result = maximumToys(prices, k)

print(result)
