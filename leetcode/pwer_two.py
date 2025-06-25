import math as m

n=int(input())
if n<=0:
    print(False)
res=str(m.log(n,2))
print(res)
if len(res) <= 5:
    print(True)
else:
    print(False)