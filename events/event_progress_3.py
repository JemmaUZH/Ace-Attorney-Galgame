from story_content import get_nickname

class EventResult:
    def __init__(self, player_choice, favor_change, dialogue_sequence, past_story=None):
        self.player_choice = player_choice
        self.favor_change = favor_change
        self.dialogue_sequence = dialogue_sequence
        self.past_story = past_story

def progress_3_event(favorability):
    # 对话序列
    dialogue_sequence = []

    # 玩家反驳的narrative（先追加到对话序列里作为旁白）
    if favorability > 65:
        narrative = "「什么男朋友！我可没喜欢过这家伙！」"
    elif favorability < 55:
        narrative = "\n「男朋友？你满脑子只有情爱吗？我是他的律师，仅此而已。」"
    else:
        narrative = "\n「你误会了，他才不是我男朋友。」"

    dialogue_sequence.append({"speaker": "Narrator", "line": narrative})
    print(narrative)

    # 选项展示
    print("【选项】\n1. 冷静分析证据\n2. 问戈多为什么突然回来\n3. 坚定维护委托人，直接反击\n")
    choice = input("输入选项编号(1-3)：")

    if choice == "1":
        player_choice_text = "冷静分析证据"
        player_line = "你抽出案件的文案，给戈多看并分析。"
        dialogue_sequence.append({"speaker": "你", "line": player_line})

        # 根据好感度动态生成戈多反应
        if favorability > 65:
            godot_line = "戈多微微一笑：「果然，你还是那个我认识的猫咪小姐。」"
            favor_change = +2
        elif favorability < 55:
            godot_line = "戈多冷笑：「现在才装冷静，有点晚了吧？」"
            favor_change = 0
        else:
            godot_line = "戈多点头：「听听你的分析吧。」"
            favor_change = +1

        dialogue_sequence.append({"speaker": "戈多", "line": godot_line})

        # 返回事件结果
        return EventResult(player_choice_text, favor_change, dialogue_sequence)


    elif choice == "2":
        dialogue_sequence.append({"speaker": "你", "line": "你凝视着他，语气沉稳「你为什么突然回来？」"})
        if favorability > 65:
            dialogue_sequence.append({"speaker": "戈多", "line": "戈多把咖啡一饮而尽：「有些真相，我只想从你口中听到。」"})
            favor_change = +1
        elif favorability < 55:
            dialogue_sequence.append({"speaker": "戈多", "line": "戈多：「呵。」"})
            favor_change = -1
        else:
            dialogue_sequence.append({
                "speaker": "戈多",
                "line": (
                    "戈多：「……咖啡之苦，非是对味蕾的惩罚，而是对心灵的邀请。\n"
                    "它领你走入暮色中的玫瑰园，\n"
                    "听潮水在远方低声吟诵逝去的誓言，\n"
                    "直到你明白，世间万物都曾以苦为名，学会生长。」"
    )
})
            favor_change = 0
        return EventResult("质问戈多的执着", favor_change, dialogue_sequence)

    elif choice == "3":
        dialogue_sequence.append({"speaker": "你", "line": "你坚定地站在被告身旁，目光毫不退缩。"})
        dialogue_sequence.append({"speaker": "戈多", "line": "戈多微微摇头「所以，你终究还是站在他那边啊……」"})
        return EventResult("坚定维护委托人", 0, dialogue_sequence)

    else:
        dialogue_sequence.append({"speaker": "你", "line": "你保持沉默，不做任何反应。"})
        dialogue_sequence.append({"speaker": "戈多", "line": f"「沉默不代表无罪，{get_nickname(favorability)}。」"})
        return EventResult("沉默", 0, dialogue_sequence)
