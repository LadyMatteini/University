num = int(input('Enter a number: '))

if num <= 0:
    print(f'Your number is: {num}')
elif num < 0:
    num * -1
    print(f'Your number is: {num}')
else:
    print('Enter a valid number')