a = input()
a = list(a)

ans = 0

if '0' not in a:
    a.pop()
    a.append('0')
else:
    for i in range(len(a)):
        if a[i] == '0':
            a[i] = '1'
            break


a = ''.join(a)
if len(a)>0:
    ans = int(a,2)


print(ans)