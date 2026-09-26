a = input()

# Please write your code here.
flag = True
a = list(a)
for i in range(len(a)):
    if a[i] == '0':
        a[i] = '1'
        flag = False
        break
if flag:
    a[-1] = '0'
a = "".join(a)

print(int(a, 2))