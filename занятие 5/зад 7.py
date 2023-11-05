def klvoo():
    klvo = -1
    a = 0
    while True:
        n = int(input())
        if n == 0:
            break
        if n > a:
            klvo += 1
        n = a
    return klvo
klvo = klvoo()
print(klvo)