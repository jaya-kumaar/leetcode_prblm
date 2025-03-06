n=int(input("enter the n:"))
res=[]
scores=[]
out=[]
for i in range(0,n):
    name =input("enter the name:")
    score=float(input("enter the grades:"))
    res.append([name,score])
    scores.append(score)    
sor_score=sorted(scores)
#print(sor_score[1])
for i in res:
    if sor_score[1] in i:
        second_lower=i[1]
        #print(second_lower)
n_list=[]
for i in res:
    for j in i:
        if second_lower == j:
            n_list.append(i[0])
n_list=sorted(n_list)
for name in n_list:
    print(name)