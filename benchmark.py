import google_tools as gt
import time

def currency_conversion(n: int, only_float_: bool = True):
    start_timer = time.time()

    for i in range(n):
        gt.currency_conversion('USD', 'BRL', only_float_)

    avg_time = (time.time() - start_timer) / n
        
    print(f"{avg_time:.3f} seconds per operation.")

def translater(n: int, source_language_: str, target_language_: str, text_: str):
    start_timer = time.time()

    for i in range(n):
        gt.translater(source_language_, target_language_, text_)

    avg_time = (time.time() - start_timer) / n
        
    print(f"{avg_time:.3f} seconds per operation.")

if __name__ == '__main__':
    currency_conversion(30) # 1.061 sec p/operation
    #currency_conversion(30, False) # 1.172 sec p/operation

    #translater(5, 'pt', 'en', 'Ola, me chamo Joao Zacchello!') # 6.293 sec p/operation
