from story_content import get_nickname

class EventResult:
    def __init__(self, player_choice,reaction, favor_change, past_story=None, narrative=""):
        self.player_choice = player_choice
        self.reaction = reaction
        self.favor_change = favor_change
        self.past_story = past_story
        self.narrative = narrative
    
        
def progress_3_event(favorability):
    #玩家反驳
    if favorability > 65:
        print("「什么男朋友！我可没喜欢过这家伙！」")
    elif favorability < 55:
        print("\n「男朋友？你满脑子只有情爱吗？我是他的律师，仅此而已。」")
    else:
        print("\n「你误会了，他才不是我男朋友。」")
    favor_change = +1
    
    print("【选项】\n1. 冷静分析证据\n2. 问戈多为什么突然回来\n3. 坚定维护委托人，直接反击")
    choice = input("输入选项编号(1-3)：")

    if choice == "1":
        reaction = [
            "你摇了摇头，「戈多，我相信他是无罪的。",
            "轻笑，「真是难得，{get_nickname()}，这么多年不见，你还是这么天真。",
            "你这么相信他，是因为律师的虚张声势，还是只是因为...」",
            "他身子前俯，话语却还带一丝玩味，「他是你的男朋友呢？」"     
        ]
        return EventResult("冷静分析证据", reaction, 1)

    elif choice == "2":
        if favorability > 65:
            reaction = "戈多把咖啡一饮而尽：「有些真相，我只想从你口中听到。」"
            favor_change = +1
        elif favorability < 55:
            reaction = "戈多：「呵。」"
            favor_change = -1
        else:
            reaction = """戈多：「...咖啡之苦，非是对味蕾的惩罚，而是对心灵的邀请。
            它领你走入暮色中的玫瑰园，
            听潮水在远方低声吟诵逝去的誓言，
            直到你明白，世间万物都曾以苦为名，学会生长。」
            """
            favor_change = 0
        return EventResult("质问戈多的执着", reaction, favor_change=favor_change)

    elif choice == "3":
        reaction = [
            "戈多：微微摇头：「所以，你终究还是站在他那边啊...」"
        ]
        return EventResult("坚定维护委托人", reaction, 0)

    else:
        reaction = [
        "「沉默不代表无罪，{get_nickname()}。"
        ]
        return EventResult("沉默", reaction, 0)

        