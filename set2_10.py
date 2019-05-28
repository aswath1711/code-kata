l=[]
i=int(input())
n=1
k=5
if i==0:
    print("0"*5,end="")
while(len(l)<k):
    if (n%i)==0:
        l.append(n)
    n+=1
print(*l)
