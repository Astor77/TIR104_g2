from pathlib import Path
import pandas as pd

json_path = Path("movie2022.json")
if json_path.exists():
    try:

    # 讀取JSON文件
        dfJSON_2022 = pd.read_json(json_path)
        #print(f"dfJSON_2022:\n{dfJSON_2022}")
        print("-----------------------------------")
    except Exception as e:
        print(f"Error reading JSON file: {e}")
else:
    print(f"File not found: {json_path}")


json_path = Path("movie2023.json")
if json_path.exists():
    try:

    # 讀取JSON文件
        dfJSON_2023 = pd.read_json(json_path)
        #print(f"dfJSON_2023:\n{dfJSON_2023}")
        print("-----------------------------------")
    except Exception as e:
        print(f"Error reading JSON file: {e}")
else:
    print(f"File not found: {json_path}")

json_path = Path("movie2024.json")
if json_path.exists():
    try:

    # 讀取JSON文件
        dfJSON_2024 = pd.read_json(json_path)
        #print(f"dfJSON_2024:\n{dfJSON_2024}")
        print("-----------------------------------")
    except Exception as e:
        print(f"Error reading JSON file: {e}")
else:
    print(f"File not found: {json_path}")

#合併2022, 2023, 2024年的資料

dfJSON = pd.concat([dfJSON_2022, dfJSON_2023, dfJSON_2024]).drop_duplicates(subset=['MovieId']).reset_index(drop=True)

# print(dfJSON)


# 只讀頭幾筆
# print(dfJSON.head()) 

# dfJSON.tail()

# dfJSON.info()

# print(dfJSON.describe())

#修改電影名稱中的() 運用split
dfJSON['Name_sp'] = dfJSON['Name'].str.split('(').str[0]
dfJSON['Name_split'] = dfJSON['Name_sp'].str.split('（').str[0]

#儲存成csv
dfJSON.to_csv('TWmovie2022-2024.csv', index = 0, encoding = 'utf-8-sig')


# print(dfJSON.loc[11, ['Name_split']])
# print(dfJSON['Name_split'])

# TWNames = dfJSON['Name_sp'].tolist()
# # print(len(TWNames))
# print(TWNames)





#轉換日期格式
def covertDate():
    # dfJSON = dfJSON.astype({'ReleaseDate': 'datetime'})
    dfJSON['ReleaseDate'] = pd.to_datetime(dfJSON["ReleaseDate"], format = '%Y-%m-%d')
    print(dfJSON['ReleaseDate'])
    print(dfJSON.dtypes)

    print(dfJSON[dfJSON['ReleaseDate'] >= '2023-01-01'])

    # print(dfJSON[['TicketRate', 'AmountRate']].mean())

def select():
    #取列值
    print(dfJSON.loc[[0,1]])
    #取欄
    print(dfJSON[['ReleaseDate', 'TheaterCount']])
    # 取列index=0以及欄位的資料
    print(dfJSON.loc[0, ['Name', 'ReleaseDate']])
    #print(dfJSON.at[0, 'Name'])

    # 取特定範圍資料
    print(dfJSON['TheaterCount'] >= 80)
    print(dfJSON[dfJSON['TheaterCount'] >= 80])

    print((dfJSON['TheaterCount'] >= 80) & (dfJSON['Region'] == '日本'))
    print(dfJSON[(dfJSON['TheaterCount'] >= 80) & (dfJSON['Region'] == '日本')])

#新增資料
def insert():
    dfJSON.loc[904] = [26666, 100, '日本' '鬼滅之刃', '2023-10-16', 400, 1000000000] #欄位數要對
    print(dfJSON.loc[904])

    #新增欄位
    dfJSON['Rating'] = 7.5
    print(dfJSON['Rating'])

#刪除資料
def delete():
    print(dfJSON.drop(904))
    # print(dfJSON.drop([2, 3]))
    #刪除欄位
    print(dfJSON.drop(columns=['Rating']))
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
    dfJSON.to_json(writeDir/"movie2023Records.json", orient="records")
    print("轉存JSON文件成功")

#轉存CSV文件
def saveCSV():
    # 存放目錄不存在就建立
    writeDir = Path("write")
    writeDir.mkdir(exist_ok= True)
    # 轉存CSV文件
    dfJSON.to_csv(writeDir/'movie_2023.csv', index = False)


# select()
# insert()
# delete()

