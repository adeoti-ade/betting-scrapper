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

from helper_functions import get_text_similarity
import warnings
warnings.filterwarnings('ignore') 



chrome_options = Options()
chrome_options.add_argument("--headless")

def load_one_x_game(game_dict={}):

    driver = webdriver.Chrome(executable_path="./chromedriver", options=chrome_options)
    driver.set_window_size(1920, 1080)  # set the window size
    driver.get('https://1xbet.ng/en/')  #get the target url

    time.sleep(5)
    # wait = WebDriverWait(driver, 20)
    time.sleep(5)

    driver.find_element_by_class_name("ls-search__button").click()
    time.sleep(5)

    data = {}
    for game in game_dict:
        driver.find_element_by_class_name("ls-filter__search")
        time.sleep(5)

        match = game_dict[game]["match"]
        print("checking for match {}".format(match))
        one_team = match.split("-")[0]
        print(one_team)

        input_field = driver.find_element_by_xpath("//input[@class='ls-search__input searchInput keyboardInput nonBorder']")
        input_field.send_keys(str(one_team))
        input_field.send_keys(Keys.ENTER)
        time.sleep(5)


        search_items = driver.find_elements_by_xpath("//div[@class='search-popup-events__item']")
        count = 0
        for item in search_items:
            teams_driver = item.find_element_by_xpath(".//div[@class='search-popup-event__teams']")
            match_text = teams_driver.text
            print(match_text)
            sim = get_text_similarity(match_text, match)
            # print(match_text, match, sim)
            # if sim >= 0.85:
            data[match+'_'+str(count)] = (match, match_text, sim)
            count += 1

        # best_selected_match = max(data, key=data.get)
        # print(best_selected_match)
    # print(data)

    return data

# driver = webdriver.Chrome(executable_path="./chromedriver", options=chrome_options)
# driver.set_window_size(1920, 1080)  # set the window size
# driver.get('https://1xbet.ng/en/')  #get the target url

# time.sleep(5)
# # wait = WebDriverWait(driver, 20)
# time.sleep(5)

# driver.find_element_by_class_name("ls-search__button").click()
# time.sleep(5)

# driver.find_element_by_class_name("ls-filter__search")
# time.sleep(5)

# input_field = driver.find_element_by_xpath("//input[@class='ls-search__input searchInput keyboardInput nonBorder']")
# input_field.send_keys(str("leeds utd"))
# input_field.send_keys(Keys.ENTER)
# time.sleep(5)


# search_items = driver.find_elements_by_xpath("//div[@class='search-popup-events__item']")
# for item in search_items:
#     teams_driver = item.find_element_by_xpath(".//div[@class='search-popup-event__teams']")
#     match_text = teams_driver.text
#     print(match_text)