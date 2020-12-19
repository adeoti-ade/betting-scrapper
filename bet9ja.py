from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.select import Select
from one_x_bet import load_one_x_game

import pandas as pd
import time 
from selenium.webdriver.common.action_chains import ActionChains



chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(executable_path="./chromedriver", options=chrome_options)
driver.set_window_size(1920, 1080)  # set the window size
driver.get('https://web.bet9ja.com/Sport/OddsToday.aspx?IDSport=590')  #get the target url
time.sleep(5)
wait = WebDriverWait(driver, 20) 

def load_game():
    bet_code = "Z92TB6B"
    driver.find_element_by_id("s_w_PC_cCoupon_txtPrenotatore").send_keys(bet_code)
    time.sleep(5)

    # load the betslip
    load = driver.find_element_by_id("s_w_PC_cCoupon_btnFakeLoadPrenotazione")
    driver.execute_script("arguments[0].style.display = 'block';", load)
    driver.execute_script("arguments[0].style.visibility = 'visible';", load)
    time.sleep(5)
    load.click()
    time.sleep(5)

    games = driver.find_elements_by_xpath("//div[@class='CItems']/div[@class='CItem te1 ']/div[@class='CSubEv']/span")
    odds = driver.find_elements_by_xpath("//div[@class='CItems']/div[@class='CItem te1 ']\
                                                /div[@class='COdds False ']/div[@class='CSegno']")
    leagues = driver.find_elements_by_xpath("//div[@class='CItems']/div[@class='CItem te1 ']/div[@class='CInfo']")
    game_dict = {}
    count = 1
    for game, odd, league in zip(games, odds, leagues):

        match_dict = {'match': game.text, 
                    'selection': odd.get_attribute('title'),
                    'league': league.get_attribute('title')}
        game_dict[f'game_{count}'] = match_dict
        count = count + 1

    driver.close()
    return game_dict

games = load_game()

data = load_one_x_game(games)

