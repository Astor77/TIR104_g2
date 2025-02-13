import requests
from lxml import html
import pandas as pd
import time
#2025存取
def numbers_movie_2025info():
    # 初始化 offset 和存放數據的空列表
    offset = 1
    data_2025 = []

    columns = [
        "Rank", "Movie", "Worldwide Box Office", "Domestic Box Office", "International Box Office", "DomesticShare"
    ]

    while True:
        # 使用 f-string 格式化 URL
        url = f"https://www.the-numbers.com/box-office-records/worldwide/all-movies/cumulative/released-in-2025/{offset}"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
        }

        response = requests.get(url, headers=headers)
        tree = html.fromstring(response.text)

        if response.status_code != 200:
            print("❌ 請求失敗，停止爬取")
            break

        print(f"開始抓取 {url}")

        # 取出表格
        movie_element = tree.xpath('//*[@id="page_filling_chart"]/center/table/tbody')

        # 確認 movie_element 是否為空，避免抓不到表格
        if not movie_element:
            print("❌ 找不到表格，停止爬取")
            break

        # 取出所有 tr 標籤，包含每一部電影的資訊
        movie_title = movie_element[0].xpath('.//tr')

        # 檢查是否有電影資料
        if not movie_title:
            print("❌ 沒有更多電影資料，停止爬取")
            break

        # 顯示調試訊息，檢查每一行的內容
        print(f"已抓取 {len(movie_title)} 部電影資料")

        # 處理每一行數據
        data = []
        for row in movie_title:
            columns_data = row.xpath('./td')  # 取得 <td> 欄位
            if len(columns_data) == 6:  # 確保每一行有 6 個欄位（原本是 5，增加 DomesticShare 欄位）
                row_data = [col.text_content().strip() for col in columns_data]
                data.append(row_data)

        # 收集數據
        data_2025.extend(data)
        offset += 100  # 下一頁

        time.sleep(2)  # 加入延遲，避免封鎖

    # 將數據轉換為 DataFrame
    df = pd.DataFrame(data_2025, columns=columns)
    df.to_csv("numbers_2025.csv", index=False, encoding="utf-8")

    print(f"✅ 完成，共 {len(df)} 筆電影資料，已儲存至 numbers_2025.csv")

#2024存取
def numbers_movie_2024info():
    # 初始化 offset 和存放數據的空列表
    offset = 1
    data_2024 = []

    columns = [
        "Rank", "Movie", "Worldwide Box Office", "Domestic Box Office", "International Box Office", "DomesticShare"
    ]

    while True:
        # 使用 f-string 格式化 URL
        url = f"https://www.the-numbers.com/box-office-records/worldwide/all-movies/cumulative/released-in-2024/{offset}"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
        }

        response = requests.get(url, headers=headers)
        tree = html.fromstring(response.text)

        if response.status_code != 200:
            print("❌ 請求失敗，停止爬取")
            break

        print(f"開始抓取 {url}")

        # 取出表格
        movie_element = tree.xpath('//*[@id="page_filling_chart"]/center/table/tbody')

        # 確認 movie_element 是否為空，避免抓不到表格
        if not movie_element:
            print("❌ 找不到表格，停止爬取")
            break

        # 取出所有 tr 標籤，包含每一部電影的資訊
        movie_title = movie_element[0].xpath('.//tr')

        # 檢查是否有電影資料
        if not movie_title:
            print("❌ 沒有更多電影資料，停止爬取")
            break

        # 顯示調試訊息，檢查每一行的內容
        print(f"已抓取 {len(movie_title)} 部電影資料")

        # 處理每一行數據
        data = []
        for row in movie_title:
            columns_data = row.xpath('./td')  # 取得 <td> 欄位
            if len(columns_data) == 6:  # 確保每一行有 6 個欄位（原本是 5，增加 DomesticShare 欄位）
                row_data = [col.text_content().strip() for col in columns_data]
                data.append(row_data)

        # 收集數據
        data_2024.extend(data)
        offset += 100  # 下一頁

        time.sleep(2)  # 加入延遲，避免封鎖

    # 將數據轉換為 DataFrame
    df = pd.DataFrame(data_2024, columns=columns)
    df.to_csv("numbers_2024.csv", index=False, encoding="utf-8")

    print(f"✅ 完成，共 {len(df)} 筆電影資料，已儲存至 numbers_2024.csv")

#2023存取
def numbers_movie_2023info():
    # 初始化 offset 和存放數據的空列表
    offset = 1
    data_2025 = []

    columns = [
        "Rank", "Movie", "Worldwide Box Office", "Domestic Box Office", "International Box Office", "DomesticShare"
    ]

    while True:
        # 使用 f-string 格式化 URL
        url = f"https://www.the-numbers.com/box-office-records/worldwide/all-movies/cumulative/released-in-2023/{offset}"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
        }

        response = requests.get(url, headers=headers)
        tree = html.fromstring(response.text)

        if response.status_code != 200:
            print("❌ 請求失敗，停止爬取")
            break

        print(f"開始抓取 {url}")

        # 取出表格
        movie_element = tree.xpath('//*[@id="page_filling_chart"]/center/table/tbody')

        # 確認 movie_element 是否為空，避免抓不到表格
        if not movie_element:
            print("❌ 找不到表格，停止爬取")
            break

        # 取出所有 tr 標籤，包含每一部電影的資訊
        movie_title = movie_element[0].xpath('.//tr')

        # 檢查是否有電影資料
        if not movie_title:
            print("❌ 沒有更多電影資料，停止爬取")
            break

        # 顯示調試訊息，檢查每一行的內容
        print(f"已抓取 {len(movie_title)} 部電影資料")

        # 處理每一行數據
        data = []
        for row in movie_title:
            columns_data = row.xpath('./td')  # 取得 <td> 欄位
            if len(columns_data) == 6:  # 確保每一行有 6 個欄位（原本是 5，增加 DomesticShare 欄位）
                row_data = [col.text_content().strip() for col in columns_data]
                data.append(row_data)

        # 收集數據
        data_2023.extend(data)
        offset += 100  # 下一頁

        time.sleep(2)  # 加入延遲，避免封鎖

    # 將數據轉換為 DataFrame
    df = pd.DataFrame(data_2023, columns=columns)
    df.to_csv("numbers_2023.csv", index=False, encoding="utf-8")

    print(f"✅ 完成，共 {len(df)} 筆電影資料，已儲存至 numbers_2023.csv")


def numbers_movie_2022info():
    # 初始化 offset 和存放數據的空列表
    offset = 1
    data_2022 = []

    columns = [
        "Rank", "Movie", "Worldwide Box Office", "Domestic Box Office", "International Box Office", "DomesticShare"
    ]

    while True:
        # 使用 f-string 格式化 URL
        url = f"https://www.the-numbers.com/box-office-records/worldwide/all-movies/cumulative/released-in-2022/{offset}"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
        }

        response = requests.get(url, headers=headers)
        tree = html.fromstring(response.text)

        if response.status_code != 200:
            print("❌ 請求失敗，停止爬取")
            break

        print(f"開始抓取 {url}")

        # 取出表格
        movie_element = tree.xpath('//*[@id="page_filling_chart"]/center/table/tbody')

        # 確認 movie_element 是否為空，避免抓不到表格
        if not movie_element:
            print("❌ 找不到表格，停止爬取")
            break

        # 取出所有 tr 標籤，包含每一部電影的資訊
        movie_title = movie_element[0].xpath('.//tr')

        # 檢查是否有電影資料
        if not movie_title:
            print("❌ 沒有更多電影資料，停止爬取")
            break

        # 顯示調試訊息，檢查每一行的內容
        print(f"已抓取 {len(movie_title)} 部電影資料")

        # 處理每一行數據
        data = []
        for row in movie_title:
            columns_data = row.xpath('./td')  # 取得 <td> 欄位
            if len(columns_data) == 6:  # 確保每一行有 6 個欄位（原本是 5，增加 DomesticShare 欄位）
                row_data = [col.text_content().strip() for col in columns_data]
                data.append(row_data)

        # 收集數據
        data_2022.extend(data)
        offset += 100  # 下一頁

        time.sleep(2)  # 加入延遲，避免封鎖

    # 將數據轉換為 DataFrame
    df = pd.DataFrame(data_2022, columns=columns)
    df.to_csv("numbers_2022.csv", index=False, encoding="utf-8")

    print(f"✅ 完成，共 {len(df)} 筆電影資料，已儲存至 numbers_2022.csv")


#numbers_movie_2022info()
#numbers_movie_2023info()
#numbers_movie_2024info()
#numbers_movie_2025info()
