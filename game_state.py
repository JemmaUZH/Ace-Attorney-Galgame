from config import character, initial_likability
from save_load import save_game, load_game

class GameState:
    """管理游戏状态，负责存取数据"""
    def __init__(self, initial_likability: int = 60):
        self.character = character
        self.likability = initial_likability
        self.progress = 1

    def introduce_character(self):
        """
        介绍人物，打印人物档案和开场白。
        """
        print("---------------------------------------------------------------")
        print("【人物档案】\n")
        for key, value in self.character.items():
            print(f"{key}：{value}")
        print("\n---------------------------------------------------------------\n")

        print("「猫咪小姐，好久不见。」\n")
        print(f"{self.character['姓名']}检察官微微一笑，目光却如同探针般刺入你的内心。\n")
        self.state = load_game() or {
            "likability": 60,
            "progress": 1,
            "log": []
        }
        
        print("---------------------------------------------------------------")
        print("【选项】")
        print("1. 表示疑惑")
        print("2. 点头微笑")
        print("3. 直接反驳")
        
    def update_state(self, result):
        """
        更新游戏状态，包括好感度和进度。

        Args:
            result (EventResult): 事件结果对象，包含好感度变化和进度推进。
        """
        self.likability += result.favor_change
        self.progress += 1
