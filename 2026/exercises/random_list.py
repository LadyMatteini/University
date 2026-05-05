import random


number = int(input('Enter a Number: '))

list = []
cont = 0


for n in range(300):
    list.append(random.randint(1, 99))

list.sort()

for n in list:
    if number == n:
        cont +=1
print(f'{list=}, {cont=}')