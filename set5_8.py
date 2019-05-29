n=int(input())
sum=0
list1=list(map(int,input().split()))
for i in range(n):
    sum=sum+list1[i]
print(sum//n)