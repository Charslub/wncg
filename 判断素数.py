n = 0
j = 2
a = int(input("请输入需要检测的前范围\n"))
b = int(input("请输入需要检测的后范围\n"))
for i in range(a, b+1):
    for j in range(2, i):
        m = i % j
        j += 1
        if m == 0:
            break
    if i == j:
        n = n + 1
        print(i, end=' ')
print("\n共有素数:", n)
