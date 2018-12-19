c = 0
b = 1
i = 0
n = int(input("请输入需要的斐波那契数列的项数"))
while i < n:
    print(b, end=' ')
    t = b
    b = c + b
    c = t
    i += 1
