from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests
from datetime import datetime

class water:
    
    def __init__(self, city_name):
        self.city_name = city_name
 
    def scrape(self):

        result = []
        
        response = requests.get("https://www.taiwanstat.com/waters/latest")

        data = response.json()
        
        return data