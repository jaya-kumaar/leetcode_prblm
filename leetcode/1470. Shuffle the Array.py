l=[1,2,3,4,5,6]
n=3
l1=l[:3]
l2=l[3:]
fl=[]
for i in range(len(l1)):
    fl.append(l1[i])
    fl.append(l2[i])
print(fl)