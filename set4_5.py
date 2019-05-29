sentence=input()
count=0
for i in sentence:
    if i.isnumeric():
        count=count+1
print(count)