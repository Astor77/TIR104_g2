from pathlib import Path
import pandas as pd
import webbrowser

year_list = [2022, 2023, 2024, 2025]

#2025年資料
# url = "https://boxofficetw.tfai.org.tw/stat/rsf/d29fa929b56c406fb2e1faf975f1c16e?filename=%E7%A5%A8%E6%88%BF%E8%B3%87%E6%96%99%E5%8C%AF%E5%87%BA%E5%B9%B4%E7%A5%A8%E6%88%BF%202025-01.json"
# webbrowser.get('windows-default').open_new(url)


#合併2022, 2023, 2024, 2025年的資料
def concat_df_json(year_list: list) -> pd.DataFrame:
    all_dfs = []  # 用來儲存每個年份的 DataFrame
    #2022-2025年資料
    for year in year_list:
        json_path = Path(f"/workspaces/TIR104_g2/Ａ_raw_data/{year} 年票房資料.json")
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

#拆為兩張表TWMovie、TWMovie_annual
def to_TWMovie_dataframe() -> pd.DataFrame:
    file_path = "/workspaces/TIR104_g2/Ａ_raw_data/TWMovie2022-2025.csv"
    dfTWMovie = pd.read_csv(file_path)


    dfTWMovie = dfTWMovie[['MovieId', 'Region', 'Name', 'ReleaseDate']]


    dfTWMovie.rename(columns= {"MovieId": "tw_id", "Region": "production_country", "Name": "tw_title", "ReleaseDate": "release_date"}, inplace= True)

    print(dfTWMovie)

    dfTWMovie.to_csv('/workspaces/TIR104_g2/Ａ_raw_data/TWMovie_df.csv', index = 0, encoding = 'utf-8-sig')

def to_TWMovie_annual_dataframe() -> pd.DataFrame:
    file_path = "/workspaces/TIR104_g2/Ａ_raw_data/TWMovie2022-2025_raw.csv"
    dfTWMovie = pd.read_csv(file_path)

    dfTWMovie_annual = dfTWMovie[['MovieId', "Year", "DayCount", "Amount", "Tickets"]]

    dfTW_count = dfTWMovie_annual.groupby(['MovieId']).count()
    print(dfTW_count)
    dfTWMovie_annual.rename(columns= {"MovieId": "tw_id", "Year": "reference_year", "DayCount": "release_days", "Amount": "reference_year_amount", "Tickets": "reference_year_tickets"}, inplace= True)
    print(dfTWMovie_annual)

    dfTWMovie_annual.to_csv('/workspaces/TIR104_g2/Ａ_raw_data/TWMovie_annual_df.csv', index = 0, encoding = 'utf-8-sig')


if __name__ == '__main__':
    combined_df = concat_df_json(year_list)
    print(combined_df.head())
    #儲存成csv
    combined_df.to_csv('/workspaces/TIR104_g2/Ａ_raw_data/TWMovie2022-2025_raw.csv', index = 0, encoding = 'utf-8-sig')

    # to_TWMovie_dataframe()
    # to_TWMovie_annual_dataframe()


#合併2022, 2023, 2024, 2025年的資料刪除重複的資料
# dfJSON = pd.concat([dfJSON_2022, dfJSON_2023, dfJSON_2024, dfJSON_2025]).drop_duplicates(subset=['MovieId']).reset_index(drop=True)

# #儲存成csv
# dfJSON.to_csv('/workspaces/TIR104_g2/Ａ_raw_data/TWMovie2022-2025.csv', index = 0, encoding = 'utf-8-sig')

# Concat_dfJSON()



# 只讀頭幾筆
# print(dfJSON.head())

# dfJSON.tail()

# dfJSON.info()

# print(dfJSON.describe())

# #修改電影名稱中的() 運用split
# dfJSON['Name_sp'] = dfJSON['Name'].str.split('(').str[0]
# dfJSON['Name_split'] = dfJSON['Name_sp'].str.split('（').str[0]

# #儲存成csv
# dfJSON.to_csv('TWmovie2022-2024.csv', index = 0, encoding = 'utf-8-sig')


# print(dfJSON.loc[11, ['Name_split']])
# print(dfJSON['Name_split'])

# TWNames = dfJSON['Name_sp'].tolist()
# # print(len(TWNames))
# print(TWNames)





#轉換日期格式
def covertDate():
    # dfJSON = dfJSON.astype({'ReleaseDate': 'datetime'})
    combined_df['ReleaseDate'] = pd.to_datetime(combined_df["ReleaseDate"], format = '%Y-%m-%d')
    print(combined_df['ReleaseDate'])
    print(combined_df.dtypes)

    print(combined_df[combined_df['ReleaseDate'] >= '2023-01-01'])

    # print(dfJSON[['TicketRate', 'AmountRate']].mean())

def select():
    #取列值
    print(combined_df.loc[[0,1]])
    #取欄
    print(combined_df[['ReleaseDate', 'TheaterCount']])
    # 取列index=0以及欄位的資料
    print(combined_df.loc[0, ['Name', 'ReleaseDate']])
    #print(dfJSON.at[0, 'Name'])

    # 取特定範圍資料
    print(combined_df['TheaterCount'] >= 80)
    print(combined_df[combined_df['TheaterCount'] >= 80])

    print((combined_df['TheaterCount'] >= 80) & (combined_df['Region'] == '日本'))
    print(combined_df[(combined_df['TheaterCount'] >= 80) & (combined_df['Region'] == '日本')])

#新增資料
def insert():
    combined_df.loc[904] = [26666, 100, '日本' '鬼滅之刃', '2023-10-16', 400, 1000000000] #欄位數要對
    print(combined_df.loc[904])

    #新增欄位
    combined_df['Rating'] = 7.5
    print(combined_df['Rating'])

#刪除資料
def delete():
    print(combined_df.drop(904))
    # print(dfJSON.drop([2, 3]))
    #刪除欄位
    print(combined_df.drop(columns=['Rating']))
    #print(dfJSON.drop('Rating', axis=1))
    #刪除所有資料
    # print(dfJSON.drop(dfJSON.index))


# 轉存JSON文件
def saveJSON():
    # 存放目錄不存在就建立
    writeDir = Path("write")
    writeDir.mkdir(exist_ok=True)
    # 轉存JSON文件
    # dfJSON.to_json(writeDir/"movie_2023.json")
    # orient="records"產生的結果不會有index
    combined_df.to_json(writeDir/"movie2023Records.json", orient="records")
    print("轉存JSON文件成功")

#轉存CSV文件
def saveCSV():
    # 存放目錄不存在就建立
    writeDir = Path("write")
    writeDir.mkdir(exist_ok= True)
    # 轉存CSV文件
    combined_df.to_csv(writeDir/'movie_2023.csv', index = False)


# select()
# insert()
# delete()

