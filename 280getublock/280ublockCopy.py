"""280blocker様
https://280blocker.net/
の当月ブロックルールを取得するだけのコードです

ブロックルールおよびフィルターについては280blocker様に従います
"""

import datetime

from selenium import webdriver
import pyautogui

dt_now_Year = datetime.datetime.now().year
strYear =str(dt_now_Year)
dt_now_Month = datetime.datetime.now().month
strMonth=str(dt_now_Month)


# ブラウザーを起動
driver = webdriver.Chrome()

driver.get('https://280blocker.net/files/280blocker_adblock_'+strYear+strMonth+'.txt')

element = driver.find_element_by_tag_name("pre")

pyautogui.keyDown('ctrl')
pyautogui.press(['a', 'c'])
pyautogui.keyUp('ctrl')

# 終了処理
driver.quit()
