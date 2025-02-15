import pandas as pd
import pymysql

# 設定 MySQL 連線資訊
DB_HOST = 'host.docker.internal'
DB_PORT = 3306  
DB_USER = 'root'
DB_PASSWORD = 'password'
DB_NAME = 'movie'
TABLE_NAME = 'movie_credits'

# 讀取 CSV 並移除不必要的欄位
file_path = "/workspaces/TIR104_g2/P_Rain/Release_Date/credits/tmdb_credits_top5_1.csv" 
df = pd.read_csv(file_path, usecols=["id", "name", "movie_id"])

# 確保 `id` 欄位不為空
df = df.dropna(subset=["id"])

# 轉換 `id` 為 int，避免 `float`
df["id"] = df["id"].astype("Int64")

# 確保 `NaN` 轉換為 `None`
df = df.astype(object).where(pd.notna(df), None)

# 連接 MySQL
conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME, charset='utf8mb4')
cursor = conn.cursor()

# 創建資料表（不設 id 為主鍵）
def create_table(cursor):
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INT,
            name VARCHAR(255),
            movie_id INT,
            entry_id INT AUTO_INCREMENT PRIMARY KEY
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    ''')

create_table(cursor)

# 插入 SQL 語法（不使用 ON DUPLICATE KEY UPDATE）
insert_query = f'''
    INSERT INTO {TABLE_NAME} (id, name, movie_id) 
    VALUES (%s, %s, %s);
'''

# 插入數據
for _, row in df.iterrows():
    try:
        print("Inserting:", (row["id"], row["name"], row["movie_id"]))  
        cursor.execute(insert_query, (row["id"], row["name"], row["movie_id"]))
    except Exception as e:
        print(f"Error inserting row {row}: {e}")

# 提交變更並關閉連線
conn.commit()
cursor.close()
conn.close()

print("CSV 資料成功匯入 MySQL！")


# import os

# print("目前工作目錄:", os.getcwd())  # 這會顯示當前 Python 執行的目錄


# import os

# folder_path = "/workspaces/TIR104_g2/P_Rain/Release_Date/credits/"
# print("該資料夾中的檔案:", os.listdir(folder_path))
