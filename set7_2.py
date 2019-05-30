n=input()
count=0
for i in n:
    if i==1 or i==0:
        continue
    else:
        count=1
if count==0:
    print("yes")
else:
    print("no")