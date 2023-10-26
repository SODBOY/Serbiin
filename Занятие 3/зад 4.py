a = int(input())
b = int(input())
l = int(input())
N = int(input())

def f1 (x,y,z,c):
    return (((c/2)-1)*x*2) + (((c/2)-1)* y * 2) + y + (2 * z)
def f2 (x,y,z):
    return min(x,y,z)
print(f2(a,b,l))