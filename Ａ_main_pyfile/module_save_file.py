import pandas as pd
import os
import json


def save_as_csv(data, file_name: str):
    """
    data: DataFrame object
    """
    file_path = "/workspaces/TIR104_g2/Ａ_raw_data/"
    csv_file_path = file_path + file_name
    data.to_csv(csv_file_path)


def save_as_json(data, file_name):
    file_path = "/workspaces/TIR104_g2/Ａ_raw_data/"
    json_file_path = file_path + file_name

    with open(json_file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)