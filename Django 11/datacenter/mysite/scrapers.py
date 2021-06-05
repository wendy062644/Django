from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests
from datetime import datetime

class CDC:
    
    def __init__(self, city_name):
        self.city_name = city_name
 
    def scrape(self):
 
        result = []
 
        response = requests.get("https://covid19dashboard.cdc.gov.tw/dash3")

        activities = response.json()['0']
        
        response = requests.get("https://covid19dashboard.cdc.gov.tw/dash7")
        
        activity = response.json()['0']
        
        response = requests.get("https://covid19dashboard.cdc.gov.tw/dash2")
        
        glo = response.json()['0']
        
        response = requests.get("https://covid19dashboard.cdc.gov.tw/dash_cases_top5")

        casetop5 = response.json()
        
        response = requests.get("https://covid19dashboard.cdc.gov.tw/dash_cases_last7_top5")

        last7casetop5 = response.json()
        
        response = requests.get("https://covid19dashboard.cdc.gov.tw/dash_deaths_top5")

        deadtop5 = response.json()
                
        result.append(
                    dict(activities = activities, activity = activity,glo = glo, casetop5 = casetop5, last7casetop5 = last7casetop5, deadtop5 = deadtop5))
        return result