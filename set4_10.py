num=int(input())
lis=[1,1]
if num<=len(lis):
    print(*lis[:num])
else:
    for i in range(2,num):
        b=lis[i-1]+lis[i-2]
        lis.append(b)
    print(*lis)