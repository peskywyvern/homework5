number = int(input('Number: '))
while number != 1:
    if number % 2 == 0:
        number = number / 2
        print(number)
    else:
        number = number*3 + 1
        print(number)
