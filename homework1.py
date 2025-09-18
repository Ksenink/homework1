ear_input = input('Введите год: ')
if len(year_input) < 4:
    print('Год должен быть четырехзначным числом')
else:
    year = int(year_input)
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print('Високосный год')
            else:
                print('Обычный год')
        else:
            print('Обычный год')
    else:
        print('Обычный год')

number_train = int(input('Номер: '))
num_one = number_train // 100000
num_two = (number_train  // 10000) % 10
num_three = (number_train  // 1000) % 10
sum_of_first_numbers = num_one + num_two + num_three
num_six = number_train % 10
num_five = (number_train % 100) // 10
num_four = (number_train % 1000) // 100
sum_of_last_numbers = num_six +num_five + num_four
if sum_of_first_numbers == sum_of_last_numbers:
    print('Счастливый билет')
else: 
    print('Несчастливый билет')

