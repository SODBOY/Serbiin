a = int(input())
b = int(input())
c = int(input())
def f1 (x,y,z):
    if x == y == z:
        print(3)
    elif x == y or y == z or z == x:
        print(2)
    else:
        print(0)
f1 (a,b,c)