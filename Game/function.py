import random
import text


# Старт игры
def start_game():
    print('\nУгадайте целое положительное число от нуля до ста, использовав десять попыток.\n')
    random_num = random.randint(0, 100)
    print(random_num)
    counter(0, random_num)


# Счетчик попыток
def counter(counter_try, random_num):
    counter_try += 1
    if counter_try > 10:
        print(f'Вы использовали все попытки, загаданное число было: {random_num}')
        return restart_game()
    inner_user_num(counter_try, random_num)


# Ввод числа пользователем и проверка ввода
def inner_user_num(counter_try, random_num):
    user_num = input('Введите целое положительное число: -> ')
    if user_num.isdigit():
        user_num = int(user_num)
        game100(counter_try, random_num, user_num)

    else:
        print('\nВы ввели не целое положительное число!')
        print(f'Вы использовали {text.text_num_try[counter_try]} попытку из десяти\n')
        counter_try += 1
        inner_user_num(counter_try, random_num)


# Основная функция игры
def game100(counter_try, random_num, user_num):
    if random_num < user_num:
        print('\nВаше число больше загаданного')

    if random_num > user_num:
        print('\nВаше число меньше загаданного')

    if random_num == user_num:
        print(f'\nВы угадали загаданное число {random_num}, использовав {text.text_num_vin[counter_try]} {text.text_num_end[counter_try]}')
        return restart_game()

    print(f'Вы использовали {text.text_num_try[counter_try]} попытку из десяти\n')

    counter(counter_try, random_num)


# Перезапуск игры
def restart_game():
    restart = input('Запустить игру сначала: (Да) -> ')
    if restart.lower() == 'да':
        start_game()
    print('Игра завершена.')

if __name__ == '__main__':
    start_game()
