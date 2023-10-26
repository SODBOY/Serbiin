n = int(input())
m = int(input())
k = int(input())
def choco(a,b,c):
    if (a*b-c)%n == 0 or (a*b-c)%m == 0:
        print('Да')
    else:
        print('Нет')
choco(n,m,k)