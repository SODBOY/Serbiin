def max():
    s = []
    n = int(input())
    while n != 0:
        s.append(n)
        n = int(input())

    max_a = 0
    a = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            a += 1
        else:
            if a > max_a:
                max_a = a

    if a > max_a:
        max_a = a

    print(max_a)
max()