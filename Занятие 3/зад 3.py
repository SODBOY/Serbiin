n = int(input())
h = n//60
m = n - h*60
if h<24:
    if len(str(h)) == 1 and len(str(m)) == 1:
        print('0',h,':','0',m)
    if len(str(h)) == 2 and len(str(m)) == 1:
        print(h, ':', '0', m)
    if len(str(h)) == 1 and len(str(m)) == 2:
        print('0',h,':',m)
    if len(str(h)) == 2 and len(str(m)) == 2:
        print(h, ':', m)
if h>24:
    if len(str(h)) == 1 and len(str(m)) == 1:
        print('0', h-24, ':', '0', m)
    if len(str(h)) == 2 and len(str(m)) == 1:
        print(h-24, ':', '0', m)
    if len(str(h)) == 1 and len(str(m)) == 2:
        print('0', h-24, ':', m)
    if len(str(h)) == 2 and len(str(m)) == 2:
        print(h-24, ':', m)
#я знаю, что не нужно было делать табло как на электронных часах, но мне стало интересно и я сделал)