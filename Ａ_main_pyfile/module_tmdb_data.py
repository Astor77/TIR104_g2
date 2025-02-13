import json
import os
import time

import pandas as pd
import requests

astor_header = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmYjIzOTQ0ZWY2ZWQyNzA1YmFlY2E4NzNmZDU4NTdiOSIsIm5iZiI6MTczNjM1NTM1My4yODgsInN1YiI6IjY3N2VhZTE5NDRkNjQ5ZmZhZTdiMTI1MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.2hnj7FRsE5MemKe5-OGGouZ2oy7pjQLEygptA0WFqpM"
            }

def get_movie_detail(tmdb_id, headers) -> json:
    """
    tmdb_id: tmdb movie id
    return json for movie detail info
    """
    try:
        url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?language=zh-TW"
        response = requests.get(url, headers=headers).json()
        return response
    except Exception as err:
        print(f"{tmdb_id} encounter {err}")
