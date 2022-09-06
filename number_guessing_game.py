import random


def compare_numbers(num, current_num):
    if num < current_num:
        return 'Wrong answer! Number you are searching for is smaller than this! Try again!'
    else:
        return 'Wrong answer! Number you are searching for is bigger than this! Try again!'


num = random.randint(0, 9)

while True:
    current_num = int(input('Enter your number: '))
    if num == current_num:
        number_found = True
        print(f'You won! The number you are searching for is {num}.')
        break
    else:
        print(compare_numbers(num, current_num))

