import random
j=0
n=int(input("请输入需要的验证码位数\n"))
m=int(input("请输入需要的验证码的个数\n"))
while j<m:
  j+=1
  def generate_verification_code(len=n):
        code_list = []
        for i in range(10):
            code_list.append(str(i))
        for i in range(65, 91):
            code_list.append(chr(i))
        for i in range(97, 123):
            code_list.append(chr(i))
            myslice = random.sample(code_list, len)
            verification_code = ''.join(myslice)
            return verification_code
  code=generate_verification_code(len=n)
  print (code)