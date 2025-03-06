from story_content import get_past_story

Class EventResult:
    def __init__(self, player_choice,reaction, favor_change, past_story):
        self.player_choice = player_choice
        self.reaction = reaction
        self.favor_change = favor_change
        self.past_story = past_story
    
    def progress_1_event(favorability):
        from utils.past_story import get_past_story

class EventResult:
    def __init__(self, player_choice, reaction, favor_change, past_story=None):
        self.player_choice = player_choice
        self.reaction = reaction  # reaction改成list，存多行
        self.favor_change = favor_change
        self.past_story = past_story

def progress_1_event(favorability):
    print("【选项】\n1. 表示疑惑\n2. 点头微笑\n3. 直接反驳")
    choice = input("输入选项编号(1-3)：")

    if choice == "1":
        reaction = [
            "\n你的脸上露出疑惑的神情：「这位先生，请问你是？」",
            "戈多举起咖啡轻酌，「才五年过去，你已经把我给忘了吗？我是戈多，现任检察官。」"
        ]
        return EventResult("表示疑惑询问他是谁", reaction, 0, get_past_story(favorability))

    elif choice == "2":
        reaction = [
            "\n你点头微笑，表示礼貌。",
            "戈多微微一笑，「看来你还记得我。」"
        ]
        return EventResult("点头微笑", reaction, 2)

    elif choice == "3":
        reaction = [
            "\n你毫不犹豫地反驳：「这位先生，我不认识你。」",
            "戈多：「哦？律师小姐，看来你贵人多忘事嘛……很好。」"
        ]
        return EventResult("直接反驳", reaction, -3)

    else:
        reaction = [
            "\n你选择沉默不语。",
            "戈多挑眉，似乎对你无言以对的操作感到意外。",
            "戈多：「什么都不说？真是有趣呢，猫咪小姐。」"
        ]
        return EventResult("沉默", reaction, 0)

        