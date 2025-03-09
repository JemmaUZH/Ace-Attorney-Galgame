import json
import os

SAVE_FILE = "save_data.json"

def save_game(state):
    """保存游戏进度"""
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=4, ensure_ascii=False)

def load_game():
    """加载游戏存档"""
    if not os.path.exists(SAVE_FILE):
        return None
    with open(SAVE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
