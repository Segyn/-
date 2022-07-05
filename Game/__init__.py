# Игра угадай число от 0 до 100
import random
import text
import function
from function import inner_user_num


def game100():
    random_num = random.randint(0, 100)
    print(random_num)
    print('\nУгадайте число использовав десять попыток\n')

    i = 0
    while i < 10:
        i += 1
        user_num = inner_user_num()

        if random_num < user_num:
            print('Ваше число больше загаданного')

        elif random_num > user_num:
            print('Ваше число меньше загаданного')

        else:
            return print(f'\nВы угадали число, использовав {text.text_num_vin[i]} {text.text_num_end[i]}')

        print(f'Вы использовали {text.text_num_try[i]} попытку из десяти\n')
    return print(f'Вы использовали все попытки, загаданное число было: {random_num}')


if __name__ == '__main__':
    game100()
