#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


import warnings
warnings.filterwarnings('ignore')


url_parent = 'http://www.cricmetric.com/playerstats.py?player=Abhishek+Sharma&role=all&format=TWENTY20&groupby=year'
player_name = 'Abhishek Sharma'
year_end = 2014
year_beg = year_end - 2

driver = webdriver.Chrome()
driver.get(url=url_parent)  # url

# Entering the player name
player_element = driver.find_element_by_id('player')
player_element.clear()
player_element.send_keys(player_name)
# player_element.send_keys(Keys.RETURN)

# Entering start year for stats
year_start_element = driver.find_element_by_id('playerStatsStartDate')
year_start_element.clear()
year_start_element.send_keys(str(year_beg)+'-01-01')
# year_start_element.send_keys(Keys.RETURN)

# Entering end year for stats
year_end_element = driver.find_element_by_id('playerStatsEndDate')
year_end_element.clear()
year_end_element.send_keys(str(year_end)+'-01-01')
# year_end_element.send_keys(Keys.RETURN)

# submitting
submit_element = driver.find_element_by_xpath(
    "/html/body/div[1]/div/div[2]/div[1]/div[2]/div/form/input[3]")
submit_element.click()

# getting overall batting stats between year_beg and year_end
# try:
#     driver.implicitly_wait(60)
#     batting_stats = driver.find_element_by_xpath(
#         '//*[@id="TWENTY20-Batting"]/div/table/tfoot/tr')
#     driver.implicitly_wait(60)
#     bat_stats = batting_stats.text.split(' ')
# except:
#     bat_stats = ['']*13
# print('Bat')
# print(bat_stats)

# # clicking on bowling tab
# try:
#     # driver.implicitly_wait(30)
#     bowling_tab_element = driver.find_element_by_id('TWENTY20-Bowling-tab')
#     bowling_tab_element.click()
#     # driver.implicitly_wait(30)
#     main = WebDriverWait(driver, 30).until(
#         EC.presence_of_element_located(
#             (By.XPATH, '//*[@id="TWENTY20-Bowling"]/div/table/tfoot/tr')))
#     bowling_stats = main.find_element_by_xpath(
#         '//*[@id="TWENTY20-Bowling"]/div/table/tfoot/tr')
#     # driver.implicitly_wait(30)
#     bowl_stats = bowling_stats.text
# except:
#     bowl_stats = ['']*13
# print('Bowl T/E')
# print(bowl_stats)

try:
    if len(driver.find_elements(By.XPATH, '//*[@id="TWENTY20-Batting"]/div/table/tfoot/tr')) > 0:
        driver.implicitly_wait(60)
        batting_stats = driver.find_element_by_xpath(
            '//*[@id="TWENTY20-Batting"]/div/table/tfoot/tr')
        driver.implicitly_wait(60)
        bat_stats = batting_stats.text.split(' ')
    else:
        bat_stats = ['']*13
except:
    bat_stats = ['']*13
print('Bat')
print(bat_stats)

# clicking on bowling tab
try:
    # driver.implicitly_wait(30)
    if len(driver.find_elements(By.XPATH, '//*[@id="TWENTY20-Batting"]/div/table/tfoot/tr')) > 0:
        bowling_tab_element = driver.find_element_by_id('TWENTY20-Bowling-tab')
        bowling_tab_element.click()
        # driver.implicitly_wait(30)
        main = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="TWENTY20-Bowling"]/div/table/tfoot/tr')))
        bowling_stats = main.find_element_by_xpath(
            '//*[@id="TWENTY20-Bowling"]/div/table/tfoot/tr')
        # driver.implicitly_wait(30)
        bowl_stats = bowling_stats.text
    else:
        bowl_stats = ['']*13
except:
    bowl_stats = ['']*13
print('Bowl T/E')
print(bowl_stats)
