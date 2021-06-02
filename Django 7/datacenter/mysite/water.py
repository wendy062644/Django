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
 
 

class water(Website):
 
    def scrape(self):
        
        result = []
        
        response = requests.get("https://chihsuan.github.io/reservoir-data/data.json")

        water = response.json()

        result.append(dict(water = water))
    
        return result