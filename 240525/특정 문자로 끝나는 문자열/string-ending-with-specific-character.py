list0=[]

for i in range(10):
    arr = input()
    list0.append(arr)

alpha = input()

for i in range(10):
    if list0[i][len(list0[i]) - 1] == alpha:
        print(list0[i])