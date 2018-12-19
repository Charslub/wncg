n = 0
for i in range(100,1000):
    t = i
    s = 0
    for j in range(0,3):
        m = t % 10
        t = t//10
        s += m*m*m
        if s == i:
            print(s, end=' ')
