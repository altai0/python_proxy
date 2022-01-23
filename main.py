
import requests
import random
import datetime
from tinydb import TinyDB
import os
import json

# example "username:password@ipadress:port"
proxieList = [
    "username:password@ipadress:port"
]

# Data Url
apiUrl = [
    'https://api.binance.com/api/v3/depth?symbol=BTCUSDT&limit=100',
    'example//url',
]


klasorAdi = []
for sas in apiUrl:
    new = sas.split('.')
    klasorAdi.append(new[1])
klasorAdi = list(dict.fromkeys(klasorAdi))

while True:
    for ix in apiUrl:
        a = datetime.datetime.now().replace(microsecond=0)
        proxy = random.choice(proxieList)
        proxiea = {
            "http": "http://" + proxy,
            "https": "http://" + proxy,
        }
        response2 = requests.get(ix,
                                 proxies=proxiea, timeout=10)
        data = response2.json()
        if response2.status_code == 200:
            nowDataName = ix.split('.')[1]
            for isak in klasorAdi:
                if isak == nowDataName:
                    fileNames = ix.split('/')
                    selam = ''.join(e for e in fileNames[-1] if e.isalnum())
                    newPath = 'C:/Users/mypc/Desktop/path/path/'+isak+'/'+selam+'.json'
                    os.makedirs(os.path.dirname(newPath), exist_ok=True)
                    item = json.dumps(data, separators=(',', ':'))
                    with open(newPath, "w") as f:
                        f.write(item)
                    b = datetime.datetime.now().replace(microsecond=0)
                    gecenSure = b - a
                    print('------------\n'+str(proxy) + ' Successfully \n' + str(
                        gecenSure) + ' second \n' + ' it is recorded ' + str(selam))
        else:
            continue
