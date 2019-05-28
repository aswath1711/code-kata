num = int(input())
s = 0
t = num
while t > 0:
   d = t % 10
   s += d ** 3
   t //= 10

if num == s:
   print("yes")
else:
   print("no")
