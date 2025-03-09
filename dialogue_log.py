import random
from config import narration_notes

class DialogueLog:
    def __init__(self):
        self.logs = []
        
    def record_log_pool(self, result):
        log_pool = []
        review = random.choice(narration_notes)

        # 【对话记录】部分
        log_pool.append("【对话记录】\n"
                        )
        for entry in result.dialogue_sequence:
            log_pool.append(f"{entry['line']}")  # 角色名已经在line里，无需加前缀

        # 记录玩家选择
        log_pool.append(f"\n【玩家选择】{result.player_choice}")

        # 记录好感度变化
        log_pool.append(f"【好感度变化】 {result.favor_change:+}\n")

        # 记录过去剧情（如果有）
        if result.past_story:
            log_pool.append(f"{result.past_story}\n")

        # 记录旁白小记
        log_pool.append(f"————旁白小记：{review}\n")

        # 保存完整日志
        full_log = "\n".join(log_pool)
        self.logs.append(full_log)

    def print_dialogue(self, final_likability):
        print("日志记录")
        print("---------------------------------------------------------------")
        for log in self.logs:
            print(log)
        print("---------------------------------------------------------------")
        print(f"Final likability: {final_likability}")
