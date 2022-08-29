################################################
# 1. Создать папку ./alphabet/ или проверить, что папка существует.
# 2. В папку ./alphabet/ поместить файлы вида a.txt, b.txt, ..., z.txt
# в которых будет записана строка алфавита, но с заменой буквы из названия файла на прописную.
# Пример: для b.txt строка будет aBcde...
# 3. Сделать щелчек Таноса - удалить случайным образом половину всех файлов в этой папке.

import os
import string
import random

def create_path(path_name):
    os.makedirs(path_name, exist_ok=True)

def create_alphabet_files():
    alphabet = string.ascii_lowercase
    for sym in alphabet:
        create_alphabet(path_name, sym, alphabet)

def create_alphabet(path_name, sym, alphabet):
    filename = os.path.join(path_name, f"{sym}.txt")
    with open(filename, "w") as file:
        file.writelines(alphabet.replace(sym, sym.upper()))

def do_tanos_click(path_name):
    files = sorted(os.listdir(path_name))
    random.shuffle(files)
    files = files[: len(files) // 2]
    for file in files:
        os.remove(os.path.join(path_name, file))


path_name = "alphabet"
create_path(path_name)
create_alphabet_files()
do_tanos_click(path_name)