# Игра угадай число от 0 до 100
import random

random_num = random.randint(0, 100)
user_num = int(input('Введите число'))


if __name__ == '__main__':
    print(random_num)
    print(user_num)
