n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
min_val = 9999999
for i in range(1, n - 1):
    tmp_x = x[0]
    tmp_y = y[0]
    tmp = 0
    for j in range(1, n):
        if j == i:
            continue
        change_x = x[j] - tmp_x if x[j] >= tmp_x else tmp_x - x[j]
        change_y = y[j] - tmp_y if y[j] >= tmp_y else tmp_y - y[j]
        tmp += change_x + change_y
        tmp_x = x[j]
        tmp_y = y[j]
    min_val = min(tmp, min_val)

print(min_val)
        