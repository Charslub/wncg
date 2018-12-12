#十进制转化为二，八，十六进制的函数调用
digit = int(input("输入一个十进制的数字\n"))
print("二进制为:", bin(digit))
print("八进制为:", oct(digit))
print("十六进制为:", hex(digit))


#二,八，十六进制转换为十进制
digital = input("请输入一串二进制字符串\n")
print("转换后的数字为:\n", int(digital, 2))
number = input("请输入一串八进制的字符串\n")
print("转换后的数字为:\n", int(number, 8))
figure = input("请输入一串十六进制的字符串\n")
print("转换后的数字为:\n", int(figure, 16))
