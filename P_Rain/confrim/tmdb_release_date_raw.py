#使用mapping_close_true.csv,跑release_dates 
import pandas as pd
import requests
import time
import os


# 讀取 mapping_close_true.csv
file_path = "v2_mapping_close_true.csv"  # 確保路徑
df = pd.read_csv(file_path)

# 檢查是否有 tmdb_id 欄位
if "id" not in df.columns:
    raise ValueError("CSV 檔案缺少 'id' 欄位！")

# 設定 TMDB API
API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MGRjN2NlNjBjNjBkODhkMDdhMGI3OWYzY2RlNjM4OCIsIm5iZiI6MTczNjkzOTg1NC4yODEsInN1YiI6IjY3ODc5OTRlYmQ3OTNjMDM1NDRmMjE3NiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-pibOcIPWjgSH1lNk_rhCRVstS21H1hV5nEPLpAdHfE"  # 這裡填入 TMDB API KEY
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "accept": "application/json"
}
BASE_URL = "https://api.themoviedb.org/3/movie/{}/release_dates"

# 儲存結果的列表
release_dates = []

# 取得唯一的 TMDB ID
_ids = df["id"].dropna().astype(int).unique()


# 查詢 API
for idx, id in enumerate(_ids):
    url = BASE_URL.format(id)
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 200:
        data = response.json()
        for result in data.get("results", []):
            country = result.get("iso_3166_1")
            for release in result.get("release_dates", []):
                release_dates.append({
                    "tmdb_id": id,
                    "country": country,
                    "certification": release.get("certification", ""),
                    "descriptors": release.get("descriptors", []),
                    "iso_639_1": release.get("iso_639_1", ""),
                    "note" : release.get("note"),
                    "release_date": release.get("release_date"),
                    "type": release.get("type")
                })

    else:
        print(f"查詢失敗: {id}, 狀態碼: {response.status_code}")

    # 加入延遲，避免 API 限制
    time.sleep(0.5)


# 轉換為 DataFrame
df_v3_release_dates = pd.DataFrame(release_dates)


# 儲存到 CSV
csv_path  = "v3_release_dates.csv"#要存的檔案位置
df_v3_release_dates.to_csv(csv_path, index=False, encoding="utf-8-sig")

# 確保 CSV 真的寫入成功
if os.path.exists("release_dates.csv"):
    print("v3_release_dates.csv 檔案成功儲存！")
else:
    print("v3_release_dates.csv 儲存失敗，請檢查權限或目錄！")