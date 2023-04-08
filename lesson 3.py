value = int(input('Ваш возраст:'))
if value > 18:
    print('Доступ к 18+ контенту открыт! Вам', value, 'лет.')
elif value == 18:
    print('Доступ к 18+ контенту открыт! Вам', value, 'лет.')
else:
    print('Доступ к 18+ контенту закрыт! Вам', value, 'лет!')

# value = int(input("Число:"))
# if value % 3 == 0 and value % 2 == 0:
#     print('Делится на 6')
# elif value % 2 == 0:
#     print('Делится на 2')
# elif value % 3 == 0:
#     print('Делится на 3')
# else:
#     print('Не делится')


# value = int(input("Число:"))
# if not value % 3 and not value % 2:
#     print('Делится на 6')
# elif not value % 2:
#     print('Делится на 2')
# elif not value % 3:
#     print('Делится на 3')
# else:
#     print('Не делится')


#
# number = int(input('Твое число:'))
# result = 'Нечётное' if (number % 2) else 'Чётное'
# print(result)


# number = int(input('Твое число:'))
# if number % 2 != 0:
#     result = number, "нечетное число"
# else:
#     result = number, 'четное число'
# print(result)



# Форматируемые строки

# value = 15
# result = (“Мне”, value, “лет”)
# print (result)
#
# преобразуем в
#
# value = 15
# result = f"Мне {value} лет!"
# print (result)


# filename = "lesson3.py"
# path = "intropython"
# print (f"D:\{path}\{filename}")


# val = 'russkiy korabl idi nahuy!'
# print(val, len(val))

# val = ''
# if len(val):
#     print (val)
# else:
#     print ("Пусто")


# val = 'russkiy nahuy'
# if "nahuy" in val:
#     print("censored")
# elif "russ":
#     print("censored")
# else:
#     print(val)

# value = "Spring"
# # print (value[5])
# print(value[-6])

# value = 10
# while value < 30:
#          print (value, "success")
#          value += 1
# else:
#     print ("stopped")


# # Игра - Угадай число от 1 до 10
#
# value = 3
# var_value = int(input("Угадай число от 1 до 10:"))
# while var_value != value:
#     if var_value > value:
#         var_value = int(input("Попробуй меньше!"))
#     elif var_value < value:
#         var_value = int(input("Попробуй больше!"))
# else:
#     print("Правильно!")
#
# count = 10
# exit_flag = True
# while exit_flag:
#     count -=1
#     if count > 0:
#         exit_flag = False
#     print("test")