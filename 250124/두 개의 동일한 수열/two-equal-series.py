n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Write your code here!

A.sort()
B.sort()

if A==B:
    print("Yes")
else:
    print("No")