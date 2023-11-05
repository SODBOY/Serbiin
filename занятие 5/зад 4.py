x = int(input())
y = int(input())
d = 1
while x <= y:
    x = x + (x*10)/100
    d = d + 1
def prtn():
    print(int(x), d)
prtn()