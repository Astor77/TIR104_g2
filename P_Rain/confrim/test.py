import os
import time

import pandas as pd
import requests


# 讀取 mapping_close_true.csv
# 讀取 CSV 檔案
def load_csv(file_path):
    df = pd.read_csv('/workspaces/TIR104_g2/P_Rain/confrim/v3_test5.csv')
    if "id" not in df.columns:
        raise ValueError("CSV 檔案缺少 'id' 欄位！")
    return df  # 修正縮排，確保函數能正確返回 df



# 取得 TMDB API 資料
def fetch_release_dates(id, headers):
    url = f"https://api.themoviedb.org/3/movie/{id}/release_dates"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        print(f"查詢失敗: {tmdb_id}, 狀態碼: {response.status_code}, 錯誤訊息: {response.text}")
        return None

# 解析 API 資料
def parse_release_dates(data, tmdb_id):
    records = []
    for result in data:
        country = result.get("iso_3166_1")
        for release in result.get("release_dates", []):
            records.append({
                "tmdb_id": id,
                "country": country,
                "certification": release.get("certification", ""),
                "descriptors": release.get("descriptors", []),
                "iso_639_1": release.get("iso_639_1", ""),
                "note": release.get("note"),
                "release_date": release.get("release_date"),
                "type": release.get("type")
            })
    return records

# 主要函數: 取得並儲存 TMDB 資料
def fetch_and_save_release_dates(input_file, output_folder):
    df = load_csv(input_file)
    API_KEY = os.getenv("TMDB_API_KEY")
    if not API_KEY:
        raise ValueError("請放置TMDB_API_KEY")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "accept": "application/json"
    }
    _ids = df["id"].dropna().astype(int).unique()
    release_dates = []
    start_time = time.time()
    for id in _ids:
        data = fetch_release_dates(id, headers)
        if data:
            release_dates.extend(parse_release_dates(data, id))
        time.sleep(1)  # 防止 API 限制

    df_releases = pd.DataFrame(release_dates)
    df_releases["release_date"] = pd.to_datetime(df_releases["release_date"], errors="coerce", utc=True)
    df_releases.dropna(subset=["release_date"], inplace=True)
    df_releases["year"] = df_releases["release_date"].dt.year.astype("Int64")
    
    os.makedirs(output_folder, exist_ok=True)
    for year, df_year in df_releases.groupby("year"):
        file_name = f"{output_folder}/release_dates_{year}.csv"
        df_year.drop(columns=["year"], inplace=True)
        df_year.to_csv(file_name, index=False, encoding="utf-8-sig")
        print(f"已儲存 {file_name}")
    
    # elapsed_time = time.time() - start_time
    # print(f"查詢完成！總共花費 {int(elapsed_time // 60)} 分 {int(elapsed_time % 60)} 秒。")

# 執行函數
if __name__ == "__main__":
    fetch_and_save_release_dates("/workspaces/TIR104_g2/P_Rain/confrim/v3_test5.csv", "release_dates_by_year")
