n,a,d=[int(x) for x in input().split()]
sum=sol=a
for i in range(n-1):
    sum=sum+d
    sol=sol+sum
print(sol)