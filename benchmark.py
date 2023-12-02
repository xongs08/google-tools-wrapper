from google_tools import GoogleTools as tools
import time

class Benchmarking:
    def currency_conversion(n: int, only_float_: bool = True):
        start_timer = time.time()

        for i in range(n):
            tools.currency_conversion('USD', 'BRL', only_float=only_float_)

        finish_timer = time.time() - start_timer
        
        print(f"{finish_timer / n} seconds per operation.")

    def translater(n: int, source_language_: str, target_language_: str, text_: str):
        start_timer = time.time()

        for i in range(n):
            tools.translater(source_language_, target_language_, text_)

        finish_timer = time.time() - start_timer
        
        print(f"{finish_timer / n} seconds per operation.")

if __name__ == '__main__':
    Benchmarking.currency_conversion(30) # 1.114 sec p/operation
    Benchmarking.currency_conversion(30, False) # 1.191 sec p/operation

    Benchmarking.translater(10, 'pt', 'en', 'Ola, me chamo Joao Zacchello!') # 6.123 sec p/operation
