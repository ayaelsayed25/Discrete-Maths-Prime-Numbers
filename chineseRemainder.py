def chinese_remainder(a, ms):
    length = len(a)
    m = 1
    for i in range(length):  #calculate m
        m = m * ms[i]
    M = []
    y = []
    sum = 0
    for i in range(length):
        M.append(m // ms[i]) #calculate M1, M2, ...Mk
        y.append(inverse(ms[i], M[i])) #get y1, y2,...yk
        sum = sum + (a[i] * M[i] * y[i])
    return sum % m


def inverse(x, y):
    if x == 0 or y == 0:
        return "Invalid"
    if x > y:
        a = x
        b = y
    else:
        a = y
        b = x
    r = b
    s = [1, 0]
    t = [0, 1]
    i = 0
    q = []
    flag = 0
    while 1:
        if i > 1:
            s.append(s[i - 2] - (q[i - 2] * s[i - 1]))
            t.append(t[i - 2] - (q[i - 2] * t[i - 1]))
        if flag:
            break
        q.append(a // b)
        i = i + 1
        if a % b == 0:
            flag = 1
            continue
        r = a % b
        a = b
        b = r
    return s[len(s) - 1]

a = [1, 2, 3, 4]
ms = [5, 7, 9, 11]
print(chinese_remainder(a, ms))