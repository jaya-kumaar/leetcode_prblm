accounts = [[1,2,3],[3,2,1]]
ma_l=[]
for i in accounts:
    ma_l.append(sum(i))
print(max(ma_l))