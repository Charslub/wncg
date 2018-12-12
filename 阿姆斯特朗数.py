n = 0
print("请输入需要检测的范围")
x = int(input("限制范围1"))
y = int(input("限制范围2"))
for i in range(x, y):
    a = len(str(i))
    t = i
    s = 0
    for j in range(0,a):
        m = t % 10
        t = t//10
        s += m**a
        if s == i:
            print(s, end=' ')
