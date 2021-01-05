
"""
Created 14.04.2020: @AJ
Collect GDP value of countries.
"""


import requests
import re
from bs4 import BeautifulSoup
from time import sleep
import threading
import random

URL_SEARCH = "https://www.google.com/search?q="
URL_COUNTRIES = "https://www.worldometers.info/geography/alphabetical-list-of-countries/"

""" Convert list of char into concatanate string """
def listCharToString(list_char):
    string = ""
    for char in list_char:
        string+= char
    return string





""" Search google """
def queryGoogle(country):
    try:
        url = URL_SEARCH +str(country) + "+gdp"
        r_google = requests.get(url)
        s_google = BeautifulSoup(r_google.content, 'html.parser')
        gdp_amount_div = s_google.find_all('div', {'class': 'BNeawe iBp4i AP7Wnd'})
        amount_gdp = gdp_amount_div[1].text
        print(country + " " +amount_gdp)
    except Exception:
        print("[EXCEPTION] for " + str(country))




""" Get all the countries name"""
def start():
    r_countries = requests.get(URL_COUNTRIES)
    s_countries = BeautifulSoup(r_countries.content, 'html.parser')
    info_country = s_countries.find_all('tr')
    for info in info_country:
        match = re.findall("[a-zA-Z]", str(info.text))
        country_name = listCharToString(match)
        if(country_name == "CountryPopulationLandAreaKmDensityPKm"):
            pass
        else:
            thread = threading.Thread(target=queryGoogle, args=(country_name,))
            thread.start()
            print(thread.name)
            rnd = random.randint(1, 2)
            sleep(rnd)



start()






