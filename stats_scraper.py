#!/usr/bin/python3

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv

import warnings
warnings.filterwarnings('ignore')


url_parent = 'http://www.cricmetric.com/playerstats.py?player=Abhishek+Sharma&role=all&format=TWENTY20&groupby=year'
url_bat = 'http://www.cricmetric.com/playerstats.py?player=abhishek+sharma&role=batsman&format=TWENTY20'
url_bowl = 'http://www.cricmetric.com/playerstats.py?player=Abhishek+Sharma&role=bowler&format=TWENTY20'
bat_file = 'data/bat_stats.csv'
bowl_file = 'data/bowl_stats.csv'


def get_bat_stats(player_names, year_ends):
    driver = webdriver.Chrome()

    for player_name, year_end in zip(player_names, year_ends):
        try:
            driver.get(url=url_bat)

            year_beg = year_end - 2
            print(
                "Batting stats of {player} for {yearst}-{yearen}".format(player=player_name, yearst=year_beg, yearen=year_end))
            # entering player name
            player_element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.ID, "player")))
            player_element.clear()
            player_element.send_keys(player_name)

            # entering start year for stats
            year_start_element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.ID, "playerStatsStartDate")))
            year_start_element.clear()
            year_start_element.send_keys(str(year_beg)+'-01-01')

            # entering start year for stats
            end_start_element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.ID, "playerStatsEndDate")))
            end_start_element.clear()
            end_start_element.send_keys(str(year_end)+'-01-01')

            # submitting
            submit_element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div[2]/div/form/input[3]")))
            submit_element.click()

            # batting stats
            try:
                if len(driver.find_elements(By.XPATH, '//*[@id="TWENTY20-Batting"]/div/table/tfoot/tr')) > 0:
                    driver.implicitly_wait(5)
                    batting_stats = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="TWENTY20-Batting"]/div/table/tfoot/tr')))
                    driver.implicitly_wait(5)
                    bat_stats = batting_stats.text.split(' ')
                    if (len(bat_stats) == 0):
                        bat_stats = ['']*13
                else:
                    bat_stats = ['']*13
            except:
                bat_stats = ['']*13
        except TimeoutException:
            bat_stats = ['']*13
            print("Time out occured. Moving on to next")

        write_list = [player_name, year_end]
        write_list.extend(bat_stats[1:])
        with open(bat_file, 'a') as bfile:
            writer = csv.writer(bfile)
            writer.writerow(write_list)
    driver.close()


def get_bowl_stats(player_names, year_ends):
    driver = webdriver.Chrome()
    for player_name, year_end in zip(player_names, year_ends):
        try:
            driver.get(url=url_bowl)
            year_beg = year_end - 2
            # entering player name
            print(
                "Bowling stats of {player} for {yearst}-{yearen}".format(player=player_name, yearst=year_beg, yearen=year_end))
            # entering player name
            player_element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.ID, "player")))
            player_element.clear()
            player_element.send_keys(player_name)

            # entering start year for stats
            year_start_element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.ID, "playerStatsStartDate")))
            year_start_element.clear()
            year_start_element.send_keys(str(year_beg)+'-01-01')

            # entering start year for stats
            end_start_element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.ID, "playerStatsEndDate")))
            end_start_element.clear()
            end_start_element.send_keys(str(year_end)+'-01-01')

            # submitting
            submit_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div[2]/div/form/input[3]")))
            submit_element.click()

            # bowling stats
            try:
                if len(driver.find_elements(By.XPATH, '//*[@id="TWENTY20-Bowling"]/div/table/tfoot/tr')) > 0:
                    driver.implicitly_wait(5)
                    bowling_stats = driver.find_element_by_xpath(
                        '//*[@id="TWENTY20-Bowling"]/div/table/tfoot/tr')
                    driver.implicitly_wait(5)
                    bowl_stats = bowling_stats.text.split(' ')
                    print(bowl_stats)
                    if (len(bowl_stats) == 0):
                        bowl_stats = ['']*13
                else:
                    bowl_stats = ['']*13
            except:
                bowl_stats = ['']*13
        except TimeoutException:
            bowl_stats = ['']*13
            print("Time out occured. Moving on to next")
        write_list = [player_name, year_end]
        write_list.extend(bowl_stats[1:])
        with open(bowl_file, 'a') as bfile:
            writer = csv.writer(bfile)
            writer.writerow(write_list)


if __name__ == '__main__':
    # player_name = ['Aaron Finch', 'Abhishek Sharma']
    # year_end = [2014, 2014]
    # get_bat_stats(player_name, year_end)
    # get_bowl_stats(player_name, year_end)
    player_year = pd.read_csv('data/player_year_cut.csv')
    players = player_year.Player.to_list()
    years = player_year.Year.to_list()
    get_bat_stats(players, years)
