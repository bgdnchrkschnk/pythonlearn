# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат.
# и возвращает список не повторяющихся цитат. Если автор не указан, цитату не брать.

import requests
import time
def get_quotes(number):
    param = {"method": 'getQuote',
    "format": "json",
    "lang": "ru",
    "key": 100}
    quotes = []
    url = "http://api.forismatic.com/api/1.0/"
    while len(quotes) < number:
        data = requests.get(url, params=param).json()
        author = data["quoteAuthor"]
        quote = data["quoteText"]
        if author and quote not in quotes:
            quotes.append(quote)
            time.sleep(1)
    return quotes
print(get_quotes(5))



# 2. Написать функцию, которая принимает результат предыдущей функции и сохраняет в csv файл.
# Имя файла сделать параметром по умолчанию.
# Заголовки csv файла:
# Author, Quote, URL.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).
# Разделитель - запятая.