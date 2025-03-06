from story_content import get_nickname

class EventResult:
    def __init__(self, player_choice, favor_change, dialogue_sequence, past_story=None):
        self.player_choice = player_choice
        self.favor_change = favor_change
        self.dialogue_sequence = dialogue_sequence
        self.past_story = past_story

def progress_2_event(favorability):
    # 对话序列
    dialogue_sequence = []

    # 开场narrative
    narrative = (
        f"戈多：「无论如何，{get_nickname(favorability)}，"
        "现在你还是头疼一下你的被告人吧，我可真羡慕他，"
        "闯出这么大的祸还要你为他收拾。」"
    )
    dialogue_sequence.append({"speaker": "Narrator", "line": narrative})

    # 选项
    print(narrative)
    print("【选项】\n1. 他是无罪的\n2. 这与你无关\n3. 是啊，他真的是很麻烦\n")
    choice = input("输入选项编号(1-3)：")

    if choice == "1":
        dialogue_sequence.append({"speaker": "你", "line": "摇了摇头：「戈多，我相信他是无罪的。」"})

        godot_line = (
            f"轻笑：「真是难得，{get_nickname(favorability)}，这么多年不见，你还是这么天真。」\n"
            "「你这么相信他，是因为律师的虚张声势，还是只是因为……」\n"
            "他身子前俯，话语却还带一丝玩味：「他是你的男朋友呢？」"
        )

        dialogue_sequence.append({"speaker": "戈多", "line": godot_line})

        return EventResult("他是无罪的", 0, dialogue_sequence)


    elif choice == "2":
        dialogue_sequence.append({"speaker": "你", "line": "只是看了他一眼：「这件事和你无关，检察官先生，我只想保护他。」"})

        godot_line = (
            f"脸上的笑容消失了，「{get_nickname(favorability)}，我从地狱爬出来，就是为了今天，可以站在这里。」\n"
            "虽然你看不到他脸上的表情，但你能感受到他在看着你。\n"
            "「怎么会与我无关呢……那就一会儿让我见识一下这个与你有关的男朋友吧。」"
        )

        dialogue_sequence.append({"speaker": "戈多", "line": godot_line})

        return EventResult("这与你无关", -3, dialogue_sequence)

    elif choice == "3":
        dialogue_sequence.append({"speaker": "你", "line": "「是啊，他真的是很麻烦」"})
        dialogue_sequence.append({"speaker": "戈多", "line": "「哦？律师小姐，看来你贵人多忘事嘛……很好。」"})
        return EventResult("是啊，他真的是很麻烦", 5, dialogue_sequence)

    else:
        dialogue_sequence.append({"speaker": "你", "line": "选择沉默不语。"})
        dialogue_sequence.append({"speaker": "戈多", "line": "「怎么了，是还在烦恼你新男朋友的案件吗？」"})
        return EventResult("沉默", 0, dialogue_sequence)
