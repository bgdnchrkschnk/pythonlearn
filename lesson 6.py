# Дана строка My name is Vova. I'm 41. But I still believe in magic. EXPELLIARMUS!
# Составить строку из больших букв этого предложения

# mystr = "My name is Vova. I'm 41. But I still believe in magic. EXPELLIARMUS!"
# for val in mystr:
#     if val

mystr = ['wd','feq','fvdv', "loxxx"]
newstr = []
for index in range(len(mystr)):
    val = mystr[index]
    if not index % 2:
        val = val.upper()
        newstr.append(val)
    else:
        val = val.lower()
        newstr.append(val)
print(newstr)


# Составить строку из маленьких букв этого предложения

# mystr = "My name is Vova. I'm 41. But I still believe in magic. EXPELLIARMUS!"
# print(mystr.lower())

# Составить строку из больших гласных букв этого предложения
# Составить строку из маленьких согласных букв этого предложения
# Составить строку из букв этого предложения, заменив большие буквы на маленькие и наоборот
# Составить строку из символов этого предложения по следующему правилу:
# Большие буквы в алфавитном порядке. Затем маленькие гласные буквы в алфавитном порядке.
# Потом маленькие согласные буквы в алфавитном порядке.
# Затем другие символы в порядке, в котором они есть в предложении.