from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests
from datetime import datetime

class water:
    
    def __init__(self, city_name):
        self.city_name = city_name
 
    def scrape(self):
        
        name = []
        maxcapa = []
        inwater = []
        outwater = []
        time = []
        high = []
        capa = []
        caparate = []
        result = []

        a = 0

        response = requests.get("https://fhy.wra.gov.tw/ReservoirPage_2011/StorageCapacity.aspx")

        data = BeautifulSoup(response.text, "lxml")

        data = data.find_all("td", limit=220)

        for activity in data:
            a = a + 1
            if a%11 == 1: name.append(dict(name = activity.getText().strip()))
            if a%11 == 2: maxcapa.append(dict(maxcapa = activity.getText().strip()))
            if a%11 == 5: inwater.append(dict(inwater = activity.getText().strip()))
            if a%11 == 6: outwater.append(dict(outwater = activity.getText().strip()))
            if a%11 == 8: time.append(dict(time = activity.getText().strip()))
            if a%11 == 9: high.append(dict(high = activity.getText().strip()))
            if a%11 == 10: capa.append(dict(capa = activity.getText().strip()))
            if a%11 == 0: caparate.append(dict(caparate = activity.getText().strip()))

        result.append(dict(name = name, maxcapa = maxcapa, inwater = inwater, outwater = outwater, time = time, high = high, capa = capa, caparate = caparate))
        return result