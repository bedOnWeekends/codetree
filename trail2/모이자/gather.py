n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
min_val = 9999999
for i in range(n):
    sum_val = 0
    for j in range(n):
        tmp = i - j if i - j >= 0 else j - i
        sum_val += tmp * A[j]
    min_val = min(min_val, sum_val)

print(min_val)