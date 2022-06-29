# Игра угадай число от 0 до 100
import random


def game100() -> str:
    random_num = random.randint(0, 100)
    print(random_num)
    
    i = 0
    while i < 10:
        user_num = int(input('Введите число '))
        if random_num < user_num:
            print('Ваше число больше')
            i += 1
        elif random_num > user_num:
            print('Ваше число меньше')
            i += 1
        else:
            print('Вы угадали')
            break


if __name__ == '__main__':
    game100()
