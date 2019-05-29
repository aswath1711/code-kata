n=input()
count1=0
count2=0
for i in n:
    if(i.isnumeric()):
        count1==1
    if(i.isalpha()):
        count2==1
if(count1==1 and count2==1):
    print("Yes")
else:
    print("No")
