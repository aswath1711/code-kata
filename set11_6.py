n,k=[int(x) for x in input().split()]
lis=list(map(int,input().split()))
odd=[]
for i in range(len(lis)):
    if(lis[i]%2)!=0:
        odd.append(lis[i])
print(odd[k-1])