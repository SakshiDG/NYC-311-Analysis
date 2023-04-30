import csv
import requests 
import os
import time
from kafka import KafkaProducer
from json import dumps
from datetime import datetime
import random 

import json

bootstrap_servers = ["localhost:9092"]
producer = KafkaProducer(bootstrap_servers=bootstrap_servers, value_serializer= lambda K: dumps(K).encode('utf-8'))



API_LINK = "https://data.cityofnewyork.us/resource/erm2-nwe9.json"

with requests.Session() as s:
    data = s.get(API_LINK).text
    dataa = json.loads(data)
    # decoded_data = link.content.decode('utf-8')
    # cr = csv.reader(decoded_data.splitlines(),delimiter=',')
    # mylist = list(cr)
    for row in dataa:
        print(f'Producing message @ {datetime.now()} | Message = {str(row)}')
        producer.send('baghwaan',row)
        time_to_sleep = random.randint(1, 10)
        time.sleep(time_to_sleep)
