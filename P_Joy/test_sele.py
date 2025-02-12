import time
import pandas as pd
import numpy as np
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

file_path = "/workspaces/TIR104_g2/Ａ_raw_data/TWMovie_df3.csv"
dfTWMovie = pd.read_csv(file_path, engine = "python")
# print(dfTWMovie)

#測試用
MovieIds = dfTWMovie["tw_id"].loc[0:1]
print(MovieIds)



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("window-size=1080,720")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-insecure-localhost")
chrome_options.add_argument("--headless")

driver = webdriver.Remote(
    command_executor="http://localhost:14444/wd/hub",
    options=chrome_options,
)
# driver = Chrome()

def get_release_date(MovieId: list) -> list:

    release_date = []
    for MovieId in MovieIds:
        try:
            data = []
            url = f"https://boxofficetw.tfai.org.tw/search/{MovieId}"
            # 連結到目標網站
            driver.get(url)
            # By種類參看 https://selenium-python.readthedocs.io/locating-elements.html
            time.sleep(3)
            elements = driver.find_elements(By.CLASS_NAME, "info")

            for element in elements:
                data.append(element.text)
                time.sleep(0.2)
            release_date.append(data[1])    
            
        except Exception as e:
            print(f"Error processing MovieId {MovieId}: {e}")
            continue  # 繼續處理下一個 MovieId
     
    # 關閉driver
    driver.close()
    return release_date


release_dates = get_release_date(MovieIds)
print(release_dates)