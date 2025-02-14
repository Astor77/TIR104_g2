import json
import os
import time

import pandas as pd
import requests

# 此模組收納用API取得原始資料的function
# 建議函式結果為原始資料

############ 全域變數
TMDB_MAIN_URL = f"https://api.themoviedb.org/3/movie/"

ASTOR_TMDB_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmYjIzOTQ0ZWY2ZWQyNzA1YmFlY2E4NzNmZDU4NTdiOSIsIm5iZiI6MTczNjM1NTM1My4yODgsInN1YiI6IjY3N2VhZTE5NDRkNjQ5ZmZhZTdiMTI1MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.2hnj7FRsE5MemKe5-OGGouZ2oy7pjQLEygptA0WFqpM"

RAIN_TMDB_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MGRjN2NlNjBjNjBkODhkMDdhMGI3OWYzY2RlNjM4OCIsIm5iZiI6MTczNjkzOTg1NC4yODEsInN1YiI6IjY3ODc5OTRlYmQ3OTNjMDM1NDRmMjE3NiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-pibOcIPWjgSH1lNk_rhCRVstS21H1hV5nEPLpAdHfE'"

ALLEN_TMDB_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkYzgwM2UyY2E0OWVlZjAxZDE3M2I4ZmEwZDZkZTQ3NCIsIm5iZiI6MTczNjk0NzYzNS45ODg5OTk4LCJzdWIiOiI2Nzg3YjdiMzgyYTY2NTQxOWViYWZlMTQiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.L3bI0Yl-M18pNoBH_Uu5EY2OdU_q1t3aTaeLr844ZR0"

WEI_TMDB_KEY = ""

VICTOR_OMDB_KEY = "de467a5d"

############

# tmdb_get_one_movie_detail()
# 抓取單部電影 detail，結果存回一個dict
def tmdb_get_one_movie_detail(tmdb_id: int, language: str="zh-TW", API_KEY: str = ASTOR_TMDB_KEY) -> dict:
    """
    抓取單一 tmdb_id 的 detail，返回 json
    Args:
        tmdb_id (int): one tmdb movie id
        headers (str): API headers 資訊，預設為 ASTOR 的API
        languages (str): 查詢的語言，預設為 zh-TW
    """
    try:
        url = f"{TMDB_MAIN_URL}{tmdb_id}?language={language}"

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "accept": "application/json"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            movie_detail = response.json()
            return movie_detail
        else:
            print(f"requests fail: {response.status_code}, tmdb_id: {tmdb_id}")
    except Exception as err:
        print(f"error: {err}, tmdb_id: {tmdb_id}")


# tmdb_get_list_movie_detail()
# 針對 movie list 抓取每一部電影 detail，結果存回一個list
def tmdb_get_list_movie_detail(tmdb_id_list: int, language: str="zh-TW", API_KEY: str = ASTOR_TMDB_KEY) -> list:
    """
    針對 movie list 抓取每一部電影 detail，返回 list
    Args:
        tmdb_id_list (list): one tmdb movie id
        headers (str): API headers 資訊，預設為 ASTOR 的API
        languages (str): 查詢的語言，預設為 zh-TW
    """
    try:
        movie_details = []
        for tmdb_id in tmdb_id_list:
            movie_details.append(tmdb_get_one_movie_detail(tmdb_id, language, API_KEY))
            time.sleep(0.5)
        return movie_details
    except Exception as err:
        print(f"tmdb_id: {tmdb_id}, error: {err}")


# tmdb_get_movie_release_date(台灣資料跟全球資料適用)


# tmdb_get_movie_credit(台灣資料跟全球資料適用)


# tmdb_get_movie_keyword(台灣資料跟全球資料適用)


# omdb_get_movie_info(台灣資料跟全球資料適用)


# tmdb_discover_movie_top500(全球資料)

