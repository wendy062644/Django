from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime

class aboutme:
    
    def __init__(self, city_name):
        self.city_name = city_name
 
    def scrape(self):

        response = requests.get("http://www.tcgs.tc.edu.tw:1218/ShowUserStatistic?account=wendy062644")

        data = BeautifulSoup(response.text, "lxml")

        data = data.find("a", {"href": "./RankList?tab=tab02&page=4#wendy062644"}).getText().strip()

        return data
