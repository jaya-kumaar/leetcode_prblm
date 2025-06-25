s="hello"
l=list(s)
l1=[]
l2=[]
n=0
for ch in l:
    l1.append(ord(ch))
print(l1)
for i in range(len(l1)-1):
    a=l1[i]-l1[i+1]
    l2.append(abs(a))
print(l2)
    
output=sum(l2)
print(output)