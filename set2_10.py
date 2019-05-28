l=[]
i=int(input())
n=1
k=5
while(len(l)<k):
    if (n%i)==0:
        l.append(n)
    n+=1
print(*l)