    
k=str(input())
a=0
for i in range(0,len(k)):
    if(k[i]!='0')and(k[i]!='1'):
        a+=1
if(a>0):
    print("no")
else:
    print("yes")
