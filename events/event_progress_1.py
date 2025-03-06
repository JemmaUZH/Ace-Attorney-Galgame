from story_content import get_past_story

class EventResult:
    def __init__(self, player_choice, favor_change, dialogue_sequence, past_story=None):
        self.player_choice = player_choice
        self.dialogue_sequence = dialogue_sequence
        self.favor_change = favor_change
        self.past_story = past_story

def progress_1_event(favorability):
    past_story = get_past_story(favorability) if favorability < 60 else None

    print("【选项】\n1. 表示疑惑\n2. 点头微笑\n3. 直接反驳\n")
    choice = input("输入选项编号(1-3)：")

    if choice == "1":
        dialogue_sequence = [
            {"speaker": "你", "line": "你的脸上露出疑惑的神情：「这位先生，请问你是？」"},
            {"speaker": "戈多", "line": "戈多举起咖啡轻酌，「才五年过去，你已经把我给忘了吗？我是戈多，现任检察官。」"}
        ]
        return EventResult("表示疑惑询问他是谁", 0, dialogue_sequence, past_story)

    elif choice == "2":
        dialogue_sequence = [
            {"speaker": "你", "line": "你点头微笑，表示礼貌。"},
            {"speaker": "戈多", "line": "戈多微微一笑，「看来你还记得我。」"}
        ]
        return EventResult("点头微笑", 2, dialogue_sequence)

    elif choice == "3":
        dialogue_sequence = [
            {"speaker": "你", "line": "你毫不犹豫地反驳「这位先生，我不认识你。」"},
            {"speaker": "戈多", "line": "「哦？律师小姐，看来你贵人多忘事嘛……很好。」"}
        ]
        return EventResult("直接反驳", -3, dialogue_sequence)

    else:
        dialogue_sequence = [
            {"speaker": "你", "line": "你选择沉默不语。"},
            {"speaker": "戈多", "line": "戈多挑眉，似乎对你无言以对的操作感到意外。"},
        ]
        return EventResult("沉默", 0, dialogue_sequence)
