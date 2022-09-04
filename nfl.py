
from cmath import log
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import json
import time

URL = 'https://www.nfl.com/stats/player-stats/'
option = Options()
driver = webdriver.Firefox()
driver.get(URL)
time.sleep(3)

element = driver.find_element(By.CLASS_NAME, "d3-o-dropdown")
element.send_keys("2021")
time.sleep(3)

driver.quit()