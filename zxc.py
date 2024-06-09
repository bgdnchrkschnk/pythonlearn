with open(file="dojd.txt", mode="r+", encoding="utf-8") as txt:
    txt.write("hgjhewf")
    global a
    a = txt.readline()
print(a)