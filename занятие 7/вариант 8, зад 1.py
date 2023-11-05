from random import randint

a = [randint(1,5) for x in range(10)]
print('Наш массив: ', a)
summa = 0
proiz = 1
for i in a:
    summa = summa + i
    proiz = proiz * i
def anton():
    print('сумма элементов массива:', summa, ' ', ' их произведение:', proiz)
anton()