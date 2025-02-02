import time
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

file_path = r"C:\Users\Shangwei Yang\Downloads\Tibame Data Engineer\PythonCrawler\Examples\WebCrawler\TWMovie2022-2025.csv"
dfTWMovie = pd.read_csv(file_path, engine = "python")



# MovieIds = dfTWMovie["MovieID"]
#測試用
MovieIds = [21945, 22241, 23147]
print(MovieIds)
#下載檔案路徑
DOWNLOAD_DIR = r"C:\Users\Shangwei Yang\Downloads\project\movie_sales"

def download_rename(MovieId: list):
    # 「./chromedriver」代表Chrome Driver檔案放在本Python程式同目錄內
    service = Service("./chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
    "download.default_directory": DOWNLOAD_DIR,  # 設定下載目錄
    "download.prompt_for_download": False,       # 自動下載
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})


    # 建立Chrome Driver
    driver = webdriver.Chrome(service=service, options=options)
    for MovieId in MovieIds:
        url = f"https://boxofficetw.tfai.org.tw/search/{MovieId}"
        # 連結到目標網站
        driver.get(url)
        # By種類參看 https://selenium-python.readthedocs.io/locating-elements.html
        # 搜尋json按鈕，然後模擬點擊該按鈕
        driver.find_element(By.XPATH, "/html/body/main/section[4]/div[1]/div/button[2]").click()
        driver.find_element(By.XPATH, "/html/body/main/section[4]/div[2]/button[3]").click()
        file_downloaded = False
        while not file_downloaded:
            time.sleep(1)  # 每秒檢查一次
            for file_name in os.listdir(DOWNLOAD_DIR):
                if file_name.endswith(".crdownload"):  # Chrome 的暫存檔案後綴
                    file_downloaded = False
                    break
                elif file_name.startswith("各週票房資料"):  # 檔案以'各週票房資料'開頭
                    original_file_path = os.path.join(DOWNLOAD_DIR, file_name)
                    new_file_path = os.path.join(DOWNLOAD_DIR, f"{MovieId}.json")  #修改檔名為{MovieId}.json
                    os.rename(original_file_path, new_file_path)
                    file_downloaded = True
                    break
        
        time.sleep(3)
    # 關閉driver
    driver.close()
        

download_rename(MovieIds)