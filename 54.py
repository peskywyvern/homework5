number = int(input('Number: '))
while True:
    if number % 2 == 0:
        number = number / 2
        print(number)
    else:
        number = number*3 + 1
        print(number)