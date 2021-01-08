def extended_euclidean(x, y):
    if x == 0 or y == 0:
        return "Invalid"
    if x > y: #a should be the greater
        a = x
        b = y
    else:
        a = y
        b = x
    r = b #initial value for r
    s = [1, 0] #define s coefficients of Bezout
    t = [0, 1] #define t coefficients of Bezout
    i = 0 #counter
    q = [] #quotient list
    flag = 0
    while 1:
        if i > 1: #start calculating s and t from i=2
            s.append(s[i - 2] - (q[i - 2] * s[i - 1]))
            t.append(t[i - 2] - (q[i - 2] * t[i - 1]))
        if flag:
            break
        q.append(a // b) #add quotient
        i = i + 1 #increase counter
        if a % b == 0:  #stopping condition : the remainder is zero
            flag = 1
            continue
        r = a % b
        a = b
        b = r
    print("s = ", s[len(s) - 1])
    print("t = ", t[len(t) - 1])
    return r


print(extended_euclidean(35, 3))
