from random import randint

a = [randint(0,3) for x in range(10)]
print('Наш массив: ', a)
summa = 0
kolvo = 0

for i in a:
    summa = summa + i
    kolvo = kolvo + 1
#    print(summa, kolvo)
srar = summa / kolvo
#print(srar)
b = [srar if x == 0 else x for x in a]

def anton():
    print('Тот же массив, но все нулевые элементы заменены на ср.арифм. нашего массива: ',b)
anton()