n,k=[int(x) for x in input().split()]
l=list(map(int,input().split()))
sum=0
for i in range(1,k+1):
    sum+=i
print(sum)