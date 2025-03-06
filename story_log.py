log = []

def record_dialogue(choice, reaction, favor_change, past_story_text=0):
    entry = f"玩家选择：{choice}\n戈多的反应：{reaction}\n好感度变化：{favor_change：+}\n"
    if past_story_text:
        entry += f"剧情回忆：{past_story_text}\n"
    log.append(entry)

def print_dialogue_log():
    print("---------------------------------------------------------------")
    print("\n【对话记录】")
    for entry in log:
        print(entry)
    print(f"(最终好感度：{favorability})")