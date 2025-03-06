from story_content import get_nickname

class EventResult:
    def __init__(self, player_choice,reaction, favor_change, past_story=None, narrative=""):
        self.player_choice = player_choice
        self.reaction = reaction
        self.favor_change = favor_change
        self.past_story = past_story
        self.narrative = narrative


def progress_2_event(favorability):
    
    narrative = f"\n戈多：「无论如何，{get_nickname(favorability)}，现在你还是头疼一下你的被告人吧，我可真羡慕他，闯出这么大的祸还要你为他收拾。」"
    print(narrative)
    
    print("【选项】\n1. 他是无罪的\n2. 这与你无关\n3. 是啊，他真的是很麻烦")
    choice = input("输入选项编号(1-3)：")

    if choice == "1":
        reaction = [
            "你摇了摇头，「戈多，我相信他是无罪的。",
            "轻笑，「真是难得，{get_nickname()}，这么多年不见，你还是这么天真。",
            "你这么相信他，是因为律师的虚张声势，还是只是因为...」",
            "他身子前俯，话语却还带一丝玩味，「他是你的男朋友呢？」"     
        ]
        return EventResult("他是无罪的", reaction, 0)

    elif choice == "2":
        reaction = [
            "你只是看了他一眼，「这件事和你无关，检察官先生，我只想保护他。」",
            "脸上的笑容消失了，「律师小姐，我从地狱爬出来，就是为了今天，可以站在这里。」",
            "虽然你看不到他脸上的表情，但你能感受到他在看着你。"
            "「怎么会与我无关呢……那就一会儿让我见识一下这个与你有关的男朋友吧。」"
        ]
        return EventResult("这与你无关", reaction, -3)

    elif choice == "3":
        reaction = [
            "你毫不犹豫地反驳：「这位先生，我不认识你。」",
            "戈多：「哦？律师小姐，看来你贵人多忘事嘛……很好。」"
        ]
        return EventResult("是啊，他真的是很麻烦", reaction, +5)

    else:
        reaction = [
            "你选择沉默不语。",
            "戈多:怎么了，是还在烦恼你新男朋友的案件吗？"
        ]
        return EventResult("沉默", reaction, 0)

        