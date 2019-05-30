num=int(input())
s=0
for i in range(2,num):
    if num%i==0:
        s=1
if s==0:
    print("yes")
else: 
    print("no")