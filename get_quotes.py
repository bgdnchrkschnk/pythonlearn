import requests
import random
import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        print(f"Time of operation: {time.time()-start_time}")
    return wrapper


class Quotes:

    __url = "https://raw.githubusercontent.com/ranjith19/random-quotes-generator/master/quotes.txt"
    def __quotes():
        return requests.get(Quotes.__url)


    def get_random_quote():
        quotes = Quotes.__quotes().text.split("\n.\n")
        status_code = Quotes.__quotes().status_code
        while True:
            yield f"Random quote from MILAN STAR:\n{random.choice(quotes)}\n\nStatus code: {status_code}"


    def filter_quote(pattern:str):
        quotes = Quotes.__quotes().text.split("\n.\n")
        status_code = Quotes.__quotes().status_code
        res = list(filter(lambda quote:pattern in quote, quotes))
        for i in res:
            yield f"{i}\nStatus code: {status_code}"

    @time_decorator
    def get_quotes(number):
        url = "https://raw.githubusercontent.com/ranjith19/random-quotes-generator/master/quotes.txt"
        quotes = requests.get(url).text.split("\n.\n")
        status_code = Quotes.__quotes().status_code
        res = [random.choice(quotes) for i in range(number)]
        print(f"\n{number} random quotes from MILAN STAR:\n")
        for i in res:
            print(f"{i}\nStatus code: {status_code}\n-----------------------------")


