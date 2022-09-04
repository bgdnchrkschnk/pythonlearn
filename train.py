# import string
# listf = [val for val in range(100) if val%2 != 0]
# print(listf)


# file = open("names.txt", "w")
# file = (file.write("Тестирую функцию записи в файл\nВроде всё ок!"))
# file_new = file
with open ("names.txt", "r") as txt:
    print(txt.read())


