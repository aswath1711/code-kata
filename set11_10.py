n,k=[int(x) for x in input().split()]
lis=list(map(int,input().split()))
lis.sort()
print(lis[k-1])