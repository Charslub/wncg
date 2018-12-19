n = int(input("请输入一个十进制的整数数字\n"))
k = int(input("请输入需要转换的进制\n"))
b = ['A', 'B', 'C', 'D', 'E', 'F']
a = []
while n != 0:
    m = n % k
    n = n // k
    if m >= 10:
        m = b[m-10]
    a.append(m)
a.reverse()
print("转换结果为:\n")
for i in a:
     print( i, end='')

