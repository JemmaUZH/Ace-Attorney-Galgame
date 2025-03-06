import random
from config import narration_notes

class DialogueLog:
    def __init__(self):
        self.logs = []
        
    def record_log_pool(self, result):
        log_pool = []
        review = random.choice(narration_notes)

        # 1. 记录完整对话sequence
        log_pool.append("【对话过程】")
        for entry in result.dialogue_sequence:
            if entry['speaker'] == "Narrator":
                log_pool.append(f"{entry['line']}")  # Narrator无需前缀
            else:
                log_pool.append(f"{entry['line']}")

        # 2. 记录玩家选择
        log_pool.append(f"【玩家选择】：{result.player_choice}")

        # 3. 好感度变化
        log_pool.append(f"【好感度变化】：{result.favor_change:+}\n")

        # 4. 过去剧情（如果有）
        if result.past_story:
            log_pool.append(f"【过去剧情】：{result.past_story}")

        # 5. 旁白小记
        log_pool.append(f"————旁白小记：{review}\n")

        # 保存到日志
        full_log = "\n".join(log_pool)
        self.logs.append(full_log)

    def print_dialogue(self, final_favorability):
        print("---------------------------------------------------------------")
        print("\n【对话记录】")
        for log in self.logs:
            print(log)
        print("---------------------------------------------------------------")
        print(f"Final favorability: {final_favorability}")
