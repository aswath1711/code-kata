l,u=[int(x) for x in input().split()]
#print(l,u)
for num in range(l,u + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num,end=" ")
