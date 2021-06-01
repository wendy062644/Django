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
 
 

class CDC(Website):
 
    def scrape(self):
 
        result = []
 
        response = requests.get("https://covid19dashboard.cdc.gov.tw/dash3")

        activities = response.json()['0']
        
        response = requests.get("https://covid19dashboard.cdc.gov.tw/dash7")
        
        activity = response.json()['0']
        
        response = requests.get("https://covid19dashboard.cdc.gov.tw/dash2")
        
        glo = response.json()['0']
 
        num1 = activities['送驗']
 
        num2 = activities['排除']
 
        num3 = activities['確診']
 
        num4 = activities['死亡']
 
        num5 = activities['解除隔離']
    
        num6 = activities['昨日送驗']
        
        num7 = activities['昨日排除']
        
        num8 = activities['昨日確診']
        
        num9 = activity['檢驗件數']
        
        num0 = activity['檢驗人數']
        
        glonum = glo['cases']
        
        glodead = glo['deaths']
        
        glocfr = glo['cfr']
        
        glocountries = glo['countries']
                
        result.append(
                    dict(num1 = num1, num2 = num2, num3 = num3, num4 = num4, num5 = num5, num6 = num6, num7 = num7, num8 = num8, num9 = num9, num0 = num0, glonum = glonum, glodead = glodead, glocfr = glocfr, glocountries = glocountries))
        return result