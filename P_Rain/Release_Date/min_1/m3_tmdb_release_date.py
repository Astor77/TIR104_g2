# #使用mapping_close_true.csv,跑release_dates 
# import pandas as pd
# import requests
# import time
# import os

# # 讀取 mapping_close_true.csv
# file_path = "/workspaces/TIR104_g2/P_Rain/Release_Date/min_1/v3_test5.csv"  # 確保路徑
# df = pd.read_csv(file_path)

# # 檢查是否有 tmdb_id 欄位
# if "id" not in df.columns:
#     raise ValueError("CSV 檔案缺少 'id' 欄位！")

# # 設定 TMDB API
# API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MGRjN2NlNjBjNjBkODhkMDdhMGI3OWYzY2RlNjM4OCIsIm5iZiI6MTczNjkzOTg1NC4yODEsInN1YiI6IjY3ODc5OTRlYmQ3OTNjMDM1NDRmMjE3NiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-pibOcIPWjgSH1lNk_rhCRVstS21H1hV5nEPLpAdHfE"  # 這裡填入 TMDB API KEY
# HEADERS = {
#     "Authorization": f"Bearer {API_KEY}",
#     "accept": "application/json"
# }
# BASE_URL = "https://api.themoviedb.org/3/movie/{}/release_dates"

# # 儲存結果的列表
# release_dates = []

# # 取得唯一的 TMDB ID
# _ids = df["id"].dropna().astype(int).unique()

# # 查詢 API
# for idx, id in enumerate(_ids):
#     url = BASE_URL.format(id)
#     response = requests.get(url, headers=HEADERS)
    
#     if response.status_code == 200:
#         data = response.json()
#         for result in data.get("results", []):
#             country = result.get("iso_3166_1")
#             for release in result.get("release_dates", []):
#                 release_dates.append({
#                     "tmdb_id": id,
#                     "country": country,
#                     "certification": release.get("certification", ""),
#                     "descriptors": release.get("descriptors", []),
#                     "iso_639_1": release.get("iso_639_1", ""),
#                     "note" : release.get("note"),
#                     "release_date": release.get("release_date"),
#                     "type": release.get("type")
#                 })

#     else:
#         print(f"查詢失敗: {id}, 狀態碼: {response.status_code}")

#     # 加入延遲，避免 API 限制
#     time.sleep(0.5)

# # 轉換為 DataFrame
# df_v3_test5_release_dates = pd.DataFrame(release_dates)

# # 儲存到 CSV
# csv_path = csv_path = "v3_test5_release_dates.csv"
# df_v3_test5_release_dates.to_csv(csv_path, index=False, encoding="utf-8-sig")

# # 確保 CSV 真的寫入成功
# if os.path.exists("release_dates.csv"):
#     print("v3_test5_release_dates.csv 檔案成功儲存！")
# else:
#     print("v3_test5_release_dates.csv 儲存失敗，請檢查權限或目錄！")

# import os

# file_path = "release_dates.csv"

# # 檢查當前目錄的所有檔案
# print("📂 目前目錄檔案列表：", os.listdir("."))

# # 確認檔案是否存在
# if os.path.exists(file_path):
#     print(f"✅ 檔案 '{file_path}' 存在！")
# else:
#     print(f"❌ 檔案 '{file_path}' 不存在，請檢查存放路徑！")

import os
import glob

# 獲取當前工作目錄
current_directory = os.getcwd()
print(f"目前工作目錄: {current_directory}")

# 搜尋所有 .csv 檔案
csv_files = glob.glob("**/v3_test5.csv", recursive=True)

# 顯示搜尋結果
if csv_files:
    print("找到 v3_test5.csv，位置如下：")
    for file in csv_files:
        print(f" {os.path.abspath(file)}")
else:
    print("未找到 v3_test5.csv，請確認是否成功儲存！")
