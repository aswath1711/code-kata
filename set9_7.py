x,y=[int(i) for i in input().split()]
if x > y:
    smaller = y
else:
    smaller = x
for i in range(1, smaller+1):
    if((x % i == 0) and (y % i == 0)):
        hcf = i
print(hcf)            



