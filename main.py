import requests
from bs4 import BeautifulSoup
import interface
import json
import database
import os
import schedule
import time 


def price_getter():
    
    
    url = 'https://www.ok.dk/privat/produkter/el/priser'
    
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    try:
        data_price = soup.find('div', class_='flex-table__cell cell--val hidden-xs')
        
        if data_price is not None:
            
            price_converter = data_price.text.strip()
            price_converter = float(price_converter.replace(',', '.'))
            price = '{:.1f}'.format(price_converter / 100)
        else:
            print("Data price isn't found!")
    except Exception as err:
        print(f"Error: {err}")
        
        
    return price 



def power_collector():

    
    #url = 'http://192.168.68.141/status'
    
    #x = requests.get(url)
    
    #y = json.loads(x.content)
    
    #d = y['merters']
    #power = (d[0]['power'])
    
    #if os.path.exists('Data.db'):
        
        #Data = database.DataCollector()
        
        #Data.insert_data(power=power)
    power = 10
    return power


def total_collector():

    
    #url = 'http://192.168.68.141/status'
    
    #power = requests.get(url)
    
    
    
    #return power
    pass
    
    


#schedule.every(1).minutes.do(power_collector)

#while 1:
    #schedule.run_pending()
    #time.sleep(1)
    
    
    
    
class calculate:
    
    def __init__(self, input):
        self.input = input
        
    def calc(self):
        
        price = price_getter()
        
        y = self.input
        
        
        x = '{:.4f}'.format(y / 1000 * price)
        
        return x
    


if __name__ == "__main__":
    try:
        interface.ui()
        e = power_collector()
        c = calculate(e)
        c.calc()
    except Exception as err:
        print(f"Error: {err}")
