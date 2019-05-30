val = input()
count=0
for ch in val:
    if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
        count=1
if(count==1):
    print("yes")
else:
    print("no")
