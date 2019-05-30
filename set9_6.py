a=input()
c=0
l=len(a)
for i in range(0,l-1):
    for j in range(i+1,l):
        if a[i]==a[j]:
            c+=1
if c==0:
    print("Yes")
else: 
	print("No")