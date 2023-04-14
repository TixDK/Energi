import requests
import json

import schedule
import time




def show_power():
    x = requests.get('http://192.168.68.141/status')

    y = json.loads(x.content)

    d = y["meters"]

    total = (d[0]['total'])
    power = (d[0]['power'])

    print(total)
    print(power)



schedule.every(5).minutes.do(show_power)

while 1:
    schedule.run_pending()
    time.sleep(1)


