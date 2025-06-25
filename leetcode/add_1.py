l=[9,9,9]
l=list(map(str,l))
l="".join(l)
l1=[]
if l[-1]!=9:
    a=int(l[-1])+1
    l1.append(a)
    print(l1)
    
elif 9 in l1:
    l1.pop()
    l1.apppend(1)
    l1.append(0)
    print(l1).split()
elif l[-1]==0:
    l1.pop()
    l1.append(1)
    print(l1)
