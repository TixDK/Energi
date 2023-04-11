#Data reader, UI



#Average price collector 

import requests
from bs4 import BeautifulSoup


url = 'https://www.ok.dk/privat/produkter/el/priser'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')


def price():
    try:
        price = soup.find('div', class_='flex-table__cell cell--val hidden-xs')
        
        if price is not None:
            data_price = price.text.strip()
            data_price = float(data_price.replace(',', '.'))
            converted_price = '{:.1f}'.format(data_price / 100)
            print(f"Average price last month is {converted_price} Danish Krones!")
        else:
            print("Price isn't found")
    except Exception as error:
        print(f"Fejl: {error}")


if __name__ == "__main__":
    price()


































