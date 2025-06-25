l=['a','a','a']
x='a'
l1=[]
for i in range(len(l)):
    if x in l[i]:
        l1.append(i)
print(l1)