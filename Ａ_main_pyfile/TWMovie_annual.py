from pathlib import Path
import pandas as pd
import webbrowser
import module_save_file as ms

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("disable-extensions")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("window-size=1080,720")
# chrome_options.add_argument("--ignore-certificate-errors")
# chrome_options.add_argument("--allow-insecure-localhost")
# chrome_options.add_argument("--headless")

# driver = webdriver.Remote(
#     command_executor="http://localhost:14444/wd/hub",
#     options=chrome_options,
# )
# driver = Chrome()

year_list = [2022, 2023, 2024, 2025]

#2025年資料需不斷更新
#這部分可能得用 selenium 處理
# url = "https://boxofficetw.tfai.org.tw/statistic/Year/10/0/all/False/Region/2025-02-14"
# webbrowser.get('windows-default').open_new(url)


#合併2022, 2023, 2024, 2025年的資料
def concat_df_json(year_list: list) -> pd.DataFrame:
    all_dfs = []  # 用來儲存每個年份的 DataFrame
    #2022-2025年資料
    for year in year_list:
        json_path = Path(f"/workspaces/TIR104_g2/Ａ_raw_data/TW/{year} 年票房資料.json")
        if json_path.exists():
            try:

            # 讀取JSON文件
                dfJSON = pd.read_json(json_path, encoding= "utf-8-sig")
                dfJSON['Year'] = f"{year}"
                all_dfs.append(dfJSON)  # 將 DataFrame 加入列表
                print(f"成功讀取: {json_path}")
                print("-----------------------------------")
            except Exception as e:
                print(f"Error reading JSON file: {e}")
        else:
            print(f"File not found: {json_path}")


    if all_dfs:
        dfJSON_raw = pd.concat(all_dfs, ignore_index=True)
        return dfJSON_raw
    else:
        print("沒有找到任何 JSON 檔案。")
        return pd.DataFrame()

#合併2022, 2023, 2024, 2025年的資料並刪除重複movieid檔案
def concat_df_json_distinct(year_list: list) -> pd.DataFrame:
    all_dfs = []  # 用來儲存每個年份的 DataFrame
    #2022-2025年資料
    for year in year_list:
        json_path = Path(f"/workspaces/TIR104_g2/Ａ_raw_data/TW/{year} 年票房資料.json")
        if json_path.exists():
            try:

            # 讀取JSON文件
                dfJSON = pd.read_json(json_path, encoding= "utf-8-sig")
                dfJSON['Year'] = f"{year}"
                all_dfs.append(dfJSON)  # 將 DataFrame 加入列表
                print(f"成功讀取: {json_path}")
                print("-----------------------------------")
            except Exception as e:
                print(f"Error reading JSON file: {e}")
        else:
            print(f"File not found: {json_path}")


    if all_dfs:
        dfJSON_distinct = pd.concat(all_dfs).drop_duplicates(subset=['MovieId']).reset_index(drop=True)
        return dfJSON_distinct
    else:
        print("沒有找到任何 JSON 檔案。")
        return pd.DataFrame()





#拆為兩張表TWMovie、TWMovie_annual
def to_TWMovie_dataframe() -> pd.DataFrame:
    file_path = "/workspaces/TIR104_g2/Ａ_raw_data/TW/TWMovie2022-2025.csv"
    dfTWMovie = pd.read_csv(file_path)


    dfTWMovie = dfTWMovie[['MovieId', 'Region', 'Name', 'ReleaseDate']]

    dfTWMovie.rename(columns= {"MovieId": "tw_id", "Region": "production_country", "Name": "tw_title", "ReleaseDate": "release_date"}, inplace= True)

    print(dfTWMovie)



def to_TWMovie_annual_dataframe() -> pd.DataFrame:
    file_path = "/workspaces/TIR104_g2/Ａ_raw_data/TW/TWMovie2022-2025_raw.csv"
    df = pd.read_csv(file_path)

    dfTWMovie_annual = df[['MovieId', "Year", "DayCount", "Amount", "Tickets"]]

    dfTW_count = dfTWMovie_annual.groupby(['MovieId']).count()
    print(dfTW_count)
    dfTWMovie_annual.rename(columns= {"MovieId": "tw_id", "Year": "reference_year", "DayCount": "release_days", "Amount": "reference_year_amount", "Tickets": "reference_year_tickets"}, inplace= True)
    print(dfTWMovie_annual)




if __name__ == '__main__':
    combined_df = concat_df_json(year_list)
    print(combined_df.head())
    #存成csv檔
    ms.save_as_csv(combined_df, "TWMovie2022-2025_raw2.csv", "TW")
    # combined_df = concat_df_json_distinct(year_list)
    # to_TWMovie_dataframe()
    # to_TWMovie_annual_dataframe()













