

import json
import time
from pydoc import html

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

URL = 'https://www.nfl.com/stats/player-stats/'
option = Options()
option.headless = True
driver = webdriver.Firefox()
driver.get(URL)
time.sleep(10)

element = driver.find_element(By.CLASS_NAME, "d3-o-dropdown")
element.send_keys('2021')
time.sleep(5)
tb = driver.find_element(By.TAG_NAME, "table").get_attribute('outerHTML')

#pegando todos os elementos com essa classe.
img = driver.find_elements(By.CLASS_NAME, "img-responsive")
img_src = []
soup = BeautifulSoup(tb, "html.parser")
df_full = pd.read_html(str(soup))[0]

df = df_full[["Player", "Pass Yds"]]


contador = 0
for i in img[1:26]:
    img_src.append((i.get_attribute("src")))
    print(i)


    




driver.quit()
