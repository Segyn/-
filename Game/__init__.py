# Игра угадай число от 0 до 100
import random


def game100() -> str:
    random_num = random.randint(0, 100)
    print(random_num)
    print('Угадайте число использовав десять попыток\n')
    i = 0
    while i < 10:
        i+=1
        user_num = int(input('Введите число '))
        if random_num < user_num:
            print('Ваше число больше загаданного')

            
        elif random_num > user_num:
            print('Ваше число меньше загаданного')
            
        else:
            print('Вы угадали')
            break
        print(f'Вы использовали {i} попыток из десяти\n')

if __name__ == '__main__':
    game100()
