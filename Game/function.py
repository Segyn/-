def inner_user_num():
    user_num=input('Введите целое положительное число: -> ')
    if user_num.isdigit():
        return int(user_num)
    else:
        print('\nВы ввели не целое положительное число\n')
        return inner_user_num()


if __name__ == '__main__':
    inner_user_num()
