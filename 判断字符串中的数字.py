print("请输入一串字符串")
a = [0]
k = 0
a = input()
for i in a:
    if i >= '0' and i <= '9':
        print(i, end=' ')
        k += 1
if k == 0:
    print("该字符串中无数字字符")
