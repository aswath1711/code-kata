n,k=list(map(int,input().split()))
lis=list(map(int,input().split()))
exist=False
for i in lis:
    if i==k:
        exist=True
        break
if exist:
    print("yes")
else:
    print("no")
