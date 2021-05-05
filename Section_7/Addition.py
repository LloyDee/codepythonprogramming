def get_average():
    print('Enter as many numbers as you want. Enter 00 to EOF')
    numbers = []
    while True:
        x = int(input('--> '))
        numbers.append(x)
        if x == 00:
            numbers.pop()
            break
    print('{:0.2f}'.format(sum(numbers) / len(numbers)))

get_average()