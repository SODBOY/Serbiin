a = int(input())
b = int(input())
c = int(input())

def minn (x,y,z):
    if x < y and x < z:
        print(x)
    elif y < x and y < z:
        print(y)
    else:
        print(z)
minn(a,b,c)