from typing import Optional, Union, List
import logging
from story_content import get_nickname

logger = logging.getLogger(__name__)

class EventResult:
    """
    事件结果类，存储玩家选择的选项、对话内容、好感度变化和过去的故事。
    
    Attributes:
        player_choice (str): 玩家选择的文本描述。
        favor_change (int): 选项对好感度的影响。
        dialogue_sequence (list[dict]): 记录游戏对话过程，每个元素是 {"speaker": str, "line": str}。
        past_story (str, optional): 过去故事内容，默认为 None。
    """   
    def __init__(self, player_choice: str, favor_change: int, dialogue_sequence: list[dict], past_story: str =None):
        self.player_choice = player_choice
        self.favor_change = favor_change
        self.dialogue_sequence = dialogue_sequence
        self.past_story = past_story

def sanitize_input(user_input:str, valid_choices: list[str])-> str:
    """
    检查用户输入是否有效，如果无效则要求用户重新输入。

    Args:
        user_input (str): 用户输入的选项编号。
        valid_choices (list[dict]): 有效选项的列表。
    
    Returns:
        str: 有效的选项编号。如果输入无效，返回“invalid”。
    """
    user_input = user_input.strip()
    if user_input and user_input.isdigit() in valid_choices:
        return user_input
    logger.warning("Invalid input. Please enter a valid choice.")
    return "invalid"


def progress_2_event(favorability: int) -> EventResult:
    """
    处理第二个剧情进展的事件。

    Args:
        favorability (int): 当前玩家的好感度。

    Returns:
        EventResult: 记录本次事件的结果，包括玩家选择的选项、对话内容和好感度变化。
    """
    
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
    logger.info(narrative)
    print("【选项】\n1. 他是无罪的\n2. 这与你无关\n3. 是啊，他真的是很麻烦\n")
    choice = input("输入选项编号(1-3)：")

    if choice == "1":
        logger.info("Player chose to believe in the defendant's innocence.")
        dialogue_sequence.append({"speaker": "你", "line": "你摇了摇头：「戈多，我相信他是无罪的。」"})

        godot_line = (
            f"戈多轻笑：「真是难得，{get_nickname(favorability)}，这么多年不见，你还是这么天真。」\n"
            "「你这么相信他，是因为律师的虚张声势，还是只是因为……」\n"
            "他身子前俯，话语却还带一丝玩味：「他是你的男朋友呢？」"
        )

        dialogue_sequence.append({"speaker": "戈多", "line": godot_line})

        return EventResult("他是无罪的", 0, dialogue_sequence)


    elif choice == "2":
        logger.info("Player chose to say 'This has nothing to do with you'.")
        dialogue_sequence.append({"speaker": "你", "line": "你只是看了他一眼：「这件事和你无关，检察官先生，我只想保护他。」"})

        godot_line = (
            f"戈多脸上的笑容消失了，「{get_nickname(favorability)}，我从地狱爬出来，就是为了今天，可以站在这里。」\n"
            "虽然你看不到他脸上的表情，但你能感受到他在看着你。\n"
            "「怎么会与我无关呢……那就一会儿让我见识一下这个与你有关的男朋友吧。」"
        )

        dialogue_sequence.append({"speaker": "戈多", "line": godot_line})

        return EventResult("这与你无关", -3, dialogue_sequence)

    elif choice == "3":
        logger.info("Player chose to say 'Yes, he is really troublesome'.")
        dialogue_sequence.append({"speaker": "你", "line": "「是啊，他真的是很麻烦」"})
        dialogue_sequence.append({"speaker": "戈多", "line": "「哦？律师小姐，看来你贵人多忘事嘛……很好。」"})
        return EventResult("是啊，他真的是很麻烦", 5, dialogue_sequence)

    else:
        logger.warning(f"Unexpected choice '{choice}', defaulting to silence.")
        dialogue_sequence.append({"speaker": "你", "line": "选择沉默不语。"})
        dialogue_sequence.append({"speaker": "戈多", "line": "「怎么了，是还在烦恼你新男朋友的案件吗？」"})
        return EventResult("沉默", 0, dialogue_sequence)
