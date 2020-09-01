from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.select import Select

import pandas as pd
import time 
from selenium.webdriver.common.action_chains import ActionChains



chrome_options = Options()
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(executable_path="./chromedriver", options=chrome_options)
driver.set_window_size(1920, 1080)  # set the window size
driver.get('https://1xbet.ng/en/')  #get the target url

time.sleep(5)

wait = WebDriverWait(driver, 20)

driver.find_element_by_class_name("ls-search__button").click()

time.sleep(5)


driver.find_element_by_class_name("ls-filter__search")