"""280blocker様
https://280blocker.net/
の当月ブロックルールを取得するだけのコードです

ブロックルールおよびフィルターについては280blocker様に従います
"""

import datetime

"""
動作環境
Chromeバージョン: 87.0.4280.88
"""
from selenium import webdriver
import chromedriver_binary

import pyautogui

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--ignore-certificate-errors')
# chromedriverのバージョンを指定
driver = webdriver.Chrome(options=options, executable_path='chromedriver.exe')

dt_now_Year = datetime.datetime.now().year
strYear =str(dt_now_Year)
dt_now_Month = datetime.datetime.now().month
strMonth=str(dt_now_Month)

if dt_now_Month<10:
    strMonth='0'+strMonth

# ブラウザーを起動
driver = webdriver.Chrome()

driver.get('https://280blocker.net/files/280blocker_adblock_'+strYear+strMonth+'.txt')

pyautogui.keyDown('ctrl')
pyautogui.press(['a', 'c'])
pyautogui.keyUp('ctrl')

# 終了処理
driver.quit()
