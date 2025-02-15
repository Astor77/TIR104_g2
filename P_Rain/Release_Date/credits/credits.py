import pandas as pd
import pymysql

# 設定 MySQL 連線資訊
DB_HOST = 'host.docker.internal'# 或者你的 MySQL 伺服器地址
DB_PORT = 3306  
DB_USER = 'root'  # 你的 MySQL 使用者名稱
DB_PASSWORD = 'password'  # 你的 MySQL 密碼
DB_NAME = 'movie'  # 你的 MySQL 資料庫名稱
TABLE_NAME = 'movie_credits'  # 你要存入的表名

# 讀取 CSV 檔案
csv_file = "/workspaces/TIR104_g2/P_Rain/Release_Date/credits/credits.csv"  # 替換為你的 CSV 檔案路徑
df = pd.read_csv(csv_file)

# # 轉換布林值（如果有需要）
# df['adult'] = df['adult'].astype(bool)

# 替換 NaN 值為 None，避免 MySQL 錯誤
# df = df.where(pd.notna(df), None)
df = df.astype(object).where(pd.notna(df), None)


def create_table(cursor):
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            movie_id INT
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    ''')

# 連接 MySQL
conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME, charset='utf8mb4')
cursor = conn.cursor()

# 創建資料表
create_table(cursor)

# 插入數據
insert_query = f'''
    INSERT INTO {TABLE_NAME} ( id,  name, movie_id) 
    VALUES (%s, %s, %s)
    ON DUPLICATE KEY UPDATE 
        name=VALUES(name),
        movie_id=VALUES(movie_id);
'''

for _, row in df.iterrows():
    cursor.execute(insert_query, tuple(row))

# 提交變更並關閉連線
conn.commit()
cursor.close()
conn.close()

print("CSV 資料成功匯入 MySQL！")
