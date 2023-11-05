print('Введите какое-нибудь число.')
n = int(input())
print(str(n)+'? Ладно,',n,'так', str(n)+'.')
s = ''
ch = [111]
for i in range(1,n+1):
    s = str(i)
    o = 0
    for ii in s:
        if int(ii) != 0:
            if i % int(ii) == 0 and ch[-1] != i:
                o = o + 1
        if len(s) == o:
            ch.append(i)
def res():
    print('Вот все числа, непревышающие '+ str(n) + ', которые делятся на каждую свою цифру:',ch[1:])
res()