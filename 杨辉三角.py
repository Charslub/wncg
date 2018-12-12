h = int(input("输入杨辉三角的行数"))
a = [0] * h
for i in range(0,h):
   for j in range(0,i+1):
      if j == 0:
          a[0] = a[i] = 1
      elif j>0 and j<i:
          a[i-j] = a[i-j] + a[i-j-1]
   k = 0
   a.append(0)
   while a[k] != 0 and k < h:
      print(a[k],end='  ')
      k+=1
   print("")