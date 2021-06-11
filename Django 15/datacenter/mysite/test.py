from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests
from datetime import datetime

class test123:
    
    def __init__(self, city_name):
        self.city_name = city_name
 
    def scrape(self):

        result = []
        
        response = requests.get("https://chihsuan.github.io/reservoir-data/data.json")

        data = response.json()

        result.append(dict(data = data))
        
        return result