import random
import text

# Название игры
print('\nУгадайте целое положительное число от нуля до ста, использовав десять попыток.\n')
# Счетчик попыток
counter_try = 0


# Ввод числа пользователем и проверка ввода
def inner_user_num():
    user_num = input('Введите целое положительное число: -> ')
    if user_num.isdigit():
        return int(user_num)
    else:
        print('\nВы ввели не целое положительное число!')
        global counter_try
        counter_try += 1
        print(f'Вы использовали {text.text_num_try[counter_try - 1]} попытку из десяти\n')
        return inner_user_num()


# Основная функция игры
def game100():
    random_num = random.randint(0, 100)
    print(random_num)
    global counter_try

    while counter_try < 10:
        counter_try += 1
        user_num = inner_user_num()

        if random_num < user_num:
            print('\nВаше число больше загаданного')

        elif random_num > user_num:
            print('\nВаше число меньше загаданного')

        else:
            return print(f'\nВы угадали загаданное число {random_num}, '
                         f'использовав {text.text_num_vin[counter_try]} {text.text_num_end[counter_try]}')

        print(f'Вы использовали {text.text_num_try[counter_try]} попытку из десяти\n')
    return print(f'Вы использовали все попытки, загаданное число было: {random_num}')


if __name__ == '__main__':
    inner_user_num()
