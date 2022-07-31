# mystr = ['wd','feq','fvdv', "loxxx"]
# newstr = []
# for index in range(len(mystr)):
#     val = mystr[index]
#     if not index % 2:
#         val = val.upper()
#         newstr.append(val)
#     else:
#         val = val.lower()
#         newstr.append(val)
#
# print(newstr)

# ###
# for index in range(len(mystr)):
#     val = mystr[index]
# ### ТОЖЕ САМОЕ ЧТО:
# for index, val in enumerate(mystr):

# Дана строка My name is Vova. I'm 41. But I still believe in magic. EXPELLIARMUS!
# Составить строку из больших букв этого предложения

# mystr = "My name is Vova. I'm 41. But I still believe in magic. EXPELLIARMUS!"
# res = []
# for val in mystr:
#     if val.isupper():
#         res.append(val)
# print("" .join(res))

# Составить строку из маленьких букв этого предложения

# mystr = "My name is Vova. I'm 41. But I still believe in magic. EXPELLIARMUS!"
# res = []
# for val in mystr:
#     if val.islower():
#         res.append(val)
# print("" .join(res))

# Составить строку из больших гласных букв этого предложения

# mystr = "My name is Vova. I'm 41. But I still believe in magic. EXPELLIARMUS!"
# res = []
# for val in mystr:
#     if val.isupper() and val.lower() in "aioue":
#         res.append(val)
# print("" .join(res))

# Составить строку из маленьких согласных букв этого предложения

# mystr = "My name is Vova. I'm 41. But I still believe in magic. EXPELLIARMUS!"
# res = []
# for val in mystr:
#     if val.islower()  and val.lower() not in "aioue":
#         res.append(val)
# print("" .join(res))

# Составить строку из букв этого предложения, заменив большие буквы на маленькие и наоборот

# mystr = "My name is Vova. I'm 41. But I still believe in magic. EXPELLIARMUS!"
# res = []
# for val in mystr:
#     if val.islower():
#         res.append(val.upper())
#     else:
#         res.append(val.lower())
# res="" .join(res)
# print(res)

# Составить строку из символов этого предложения по следующему правилу:
# Большие буквы в алфавитном порядке. Затем маленькие гласные буквы в алфавитном порядке.
# Потом маленькие согласные буквы в алфавитном порядке.
# Затем другие символы в порядке, в котором они есть в предложении.


mystr = "My name is Vova. I'm 41. But I still believe in magic. EXPELLIARMUS!"
str1 = []
str2 = []
str3 = []
str4 = []
res = []
for val in mystr:
    if val.isupper():
        str1.append(val)
        str1.sort()
    elif val in "aoueyi":
        str2.append(val)
        str2.sort()
    elif val.isalpha():
        str3.append(val)
        str3.sort()
    else:
        str4.append(val)
res = str1+str2+str3+str4
res = "".join(res)
print(res, type(res))