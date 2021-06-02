from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests
from datetime import datetime

class Website(ABC):
 
    def __init__(self, city_name):
        self.city_name = city_name
 
    @abstractmethod
    def scrape(self):
        pass
 
 

class test123(Website):
 
    def scrape(self):
        
        result = []
        
        response = requests.get("https://covid19dashboard.cdc.gov.tw/dash_cases_top5")

        casetop5 = response.json()

        result.append(dict(casetop5 = casetop5))
    
        return result