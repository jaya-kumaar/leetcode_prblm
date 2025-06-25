nums=[0,2,2,0]
l1=[]
l2=[]
for i in nums:
    if i not in l1:
        l1.append(i)
    elif i in l1:
        l2.append(i)
print(l2)