str=input()
l=[]
for i in str:
    if i.isnumeric():
        l.append(i)
print("".join(l))        