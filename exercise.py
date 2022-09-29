import re

a = "Bogdan Cherkashchenko"
res = re.split(" ",a)
if len(res) > 1:
    print("yes")
print(res)