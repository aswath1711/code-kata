sentence=input()
count=0
for i in sentence :
  if i.isnumeric()!=True :
    if i.isalpha()!=True :
      count=count+1
print(count)