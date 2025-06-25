# s=input()
# ls=list(s)
# v=[]
# roman= {
#     "M": 1000,
#     "D": 500,
#     "C": 100,
#     "L": 50,
#     "X": 10,
#     "V": 5,
#     "I": 1,
# }

# for ch in ls:
#     v.append(roman[ch])
# print(sum(v))
s=input()
curr = 0
total = 0

roman = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1,
}

for ch in reversed(s):
    if ch not in roman:
        print({ch})
        exit()
    curr = roman[ch]
    if curr < total:
        total -= curr
    else:
        total += curr

print(total)
