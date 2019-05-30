a=input()
w=[]
for i in a:
    w.append(i)
b=len(w)
v=b//2
if(b%2!=0):
    w[v]="*"
else:
    w[v]="*"
    w[v-1]="*"
print("".join(w))