import pandas as pd
import json

# 讀取上傳的 JSON 檔案
file_path = "/workspaces/TIR104_g2/P_Rain/confrim/iso3166_country.json"

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# 擷取需要的欄位
countries_data = [
    {
        "release_country_name": item["name"],
        "release_country_code": item["twoLetterCode"],
        "Traditional Chinese Name": item["traditionalChineseName"],
    }
    for item in data["list"]
]

# 轉換為 DataFrame
df = pd.DataFrame(countries_data)

# 保存為 CSV 檔案
csv_file_path = "iso3166_country.csv"
df.to_csv(csv_file_path, index=False, encoding="utf-8-sig")

# import sys
# print("Hello", file=sys.stderr)  # 強制輸出到錯誤訊息流
