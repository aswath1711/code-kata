
def sort(a, start, end):
    if end - start > 1:
        p = div(a, start, end)
        sort(a, start, p)
        sort(a, p + 1, end)
 
 
def div(alist, start, end):
    p = a[start]
    i = start + 1
    j = end - 1
 
    while True:
        while (i <= j and a[i] <= p):
            i = i + 1
        while (i <= j and a[j] >= p):
            j = j - 1
 
        if i <= j:
            a[i], a[j] = a[j], a[i]
        else:
            a[start], a[j] = a[j], a[start]
            return j
 
mum=int(input())
a = input().split()
a= [int(x) for x in a]
sort(a, 0, len(a))
print(*a)