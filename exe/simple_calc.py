# Просим пользователя ввести число.

def get_input():
    print('\n')

    number = 0

    try:
        number = int(input('Input a number: '))

    except ValueError:
        print('INPUT ERROR')
        print('CLOSING THE APP')

    return number


# Просим пользователя выбрать операцию.

def get_operator():

    x = 1

    # Помещаем функцию ввода внутри цикла. Цикл повторяется покуда пользователь не введёт требуемое значение.

    while x == 1:

        print('\n')
        operator = input('Choose an operation +, -, *, /  ')

        if operator == '+' or operator == '-' or operator == '*' or operator == '/':
            return operator

        else:
            print('\n')
            print('Wrong input, try again')


# Получаем пользовательский ввод

def get_result(input_1, operator, input_2):

    if operator == '+':
        return input_1 + input_2

    if operator == '-':
        return input_1 - input_2

    if operator == '*':
        return input_1 * input_2

    if operator == '/':
        return input_1 / input_2


# Выводим результаты на экран

def print_result(input_1, input_2, operator, result):

    if operator == '+':
        print('\n')
        print(f'{input_1} + {input_2} = {result}')

    if operator == '-':
        print('\n')
        print(f'{input_1} - {input_2} = {result}')

    if operator == '*':
        print('\n')
        print(f'{input_1} * {input_2} = {result}')

    if operator == '/':
        print('\n')
        print(f'{input_1} / {input_2} = {result}')


# Помещаем все вызовы функций в главную функцию

def main():
    input_1 = get_input()
    operator = get_operator()
    input_2 = get_input()
    result = get_result(input_1, operator, input_2)
    print_result(input_1, input_2, operator, result)
    print('\n')
    input("Нажмите \"Enter\" для закрытия программы.")


main()
