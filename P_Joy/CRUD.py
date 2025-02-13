# #轉換日期格式
# def covertDate():
#     # dfJSON = dfJSON.astype({'ReleaseDate': 'datetime'})
#     combined_df['ReleaseDate'] = pd.to_datetime(combined_df["ReleaseDate"], format = '%Y-%m-%d')
#     print(combined_df['ReleaseDate'])
#     print(combined_df.dtypes)

#     print(combined_df[combined_df['ReleaseDate'] >= '2023-01-01'])

#     # print(dfJSON[['TicketRate', 'AmountRate']].mean())

# def select():
#     #取列值
#     print(combined_df.loc[[0,1]])
#     #取欄
#     print(combined_df[['ReleaseDate', 'TheaterCount']])
#     # 取列index=0以及欄位的資料
#     print(combined_df.loc[0, ['Name', 'ReleaseDate']])
#     #print(dfJSON.at[0, 'Name'])

#     # 取特定範圍資料
#     print(combined_df['TheaterCount'] >= 80)
#     print(combined_df[combined_df['TheaterCount'] >= 80])

#     print((combined_df['TheaterCount'] >= 80) & (combined_df['Region'] == '日本'))
#     print(combined_df[(combined_df['TheaterCount'] >= 80) & (combined_df['Region'] == '日本')])

# #新增資料
# def insert():
#     combined_df.loc[904] = [26666, 100, '日本' '鬼滅之刃', '2023-10-16', 400, 1000000000] #欄位數要對
#     print(combined_df.loc[904])

#     #新增欄位
#     combined_df['Rating'] = 7.5
#     print(combined_df['Rating'])

# #刪除資料
# def delete():
#     print(combined_df.drop(904))
#     # print(dfJSON.drop([2, 3]))
#     #刪除欄位
#     print(combined_df.drop(columns=['Rating']))
#     #print(dfJSON.drop('Rating', axis=1))
#     #刪除所有資料
#     # print(dfJSON.drop(dfJSON.index))


# # 轉存JSON文件
# def saveJSON():
#     # 存放目錄不存在就建立
#     writeDir = Path("write")
#     writeDir.mkdir(exist_ok=True)
#     # 轉存JSON文件
#     # dfJSON.to_json(writeDir/"movie_2023.json")
#     # orient="records"產生的結果不會有index
#     combined_df.to_json(writeDir/"movie2023Records.json", orient="records")
#     print("轉存JSON文件成功")

# #轉存CSV文件
# def saveCSV():
#     # 存放目錄不存在就建立
#     writeDir = Path("write")
#     writeDir.mkdir(exist_ok= True)
#     # 轉存CSV文件
#     combined_df.to_csv(writeDir/'movie_2023.csv', index = False)


# # select()
# # insert()
# # delete()