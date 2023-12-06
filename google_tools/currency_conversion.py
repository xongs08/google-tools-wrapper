from bs4 import BeautifulSoup as bs # html parser
from requests import get # requesting site

def wrapper(url):
    resp = get(url)
    soup = bs(resp.content, 'html.parser')
    return soup

def currency_conversion(base_currency: str, target_currency: str, only_float: bool = True) -> tuple | dict:
    url_ = f"https://www.google.com/finance/quote/{base_currency.upper()}-{target_currency.upper()}" # base url

    soup = wrapper(url_)
        
    currency_value = float(soup.find('div', attrs={'class': 'YMlKec fxKbKc'}).text) # find the value of the currency and turn into a float

    last_update = soup.find('div', attrs={'class': 'ygUjEc', 'jsname': 'Vebqub'}).text.replace('\u202f', ' ').replace(' · Disclaimer', '') # finding the last update of the currency and filter it to remove bullshit

    conversion_dict = { # formatting the wrapped data to return it prettyfied
        'conversion': [
            f'1 {base_currency}',
            f'{currency_value:.2f} {target_currency}'
        ],
        'float': currency_value,
        'last_update': last_update
    }

    if only_float is not True: # filtering return
        return conversion_dict
    else:
        return conversion_dict['float']
