nums=[1,2,3,9,4,4,1,2]
dict={}
for i in range(len(nums)):
    dict[i]=nums.count(i)
for key, value in dict.items():
    if value == 1:
        print(key)
