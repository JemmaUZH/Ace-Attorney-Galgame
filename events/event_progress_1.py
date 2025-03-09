from typing import Optional, Union, List
import logging
from story_content import get_past_story

logger = logging.getLogger(__name__)

class EventResult:
    """
    事件结果类，存储玩家选择的选项、对话内容、好感度变化和过去的故事。
    
    Attributes:
        player_choice (str): 玩家选择的文本描述。
        favor_change (int): 选项对好感度的影响。
        dialogue_sequence (List[Dict[str, str]]): 记录游戏对话过程，每个元素是 {"speaker": str, "line": str}。
        past_story (Optional[str]): 过去故事内容，默认为 None。
    """   
    def __init__(self, player_choice: str, favor_change: int, dialogue_sequence: List[Dict[str, str]], past_story: Optional[str] = None):
        self.player_choice = player_choice
        self.dialogue_sequence = dialogue_sequence
        self.favor_change = favor_change
        self.past_story = past_story

def sanitize_input(user_input: str, valid_choices: List[str]) -> str:
    """
    处理用户输入，确保其为有效的选项。

    Args:
        user_input (str): 用户输入的值。
        valid_choices (List[str]): 可接受的选项列表。

    Returns:
        str: 经过处理后的选项。如果输入无效，返回 "invalid"。
    """
    user_input = user_input.strip()  # 去除空格
    if user_input.isdigit() and user_input in valid_choices:
        return user_input
    logger.warning(f"无效输入: {user_input}")
    return "invalid"


def progress_1_event(favorability: int) -> EventResult:
    """
    处理第一个剧情进展的事件。

    Args:
        favorability (int): 当前玩家的好感度。

    Returns:
        EventResult: 记录本次事件的结果，包括玩家选择的选项、对话内容和好感度变化。
    """
       
    
    past_story = get_past_story(favorability) if favorability < 60 else None
    choice = input("输入选项编号(1-3)：")

    if choice == "1":
        logger.info("Player chose to express confusion and ask who he is.")
        dialogue_sequence = [
            {"speaker": "你", "line": "你的脸上露出疑惑的神情：「这位先生，请问你是？」"},
            {"speaker": "戈多", "line": "戈多举起咖啡轻酌，「才五年过去，你已经把我给忘了吗？我是戈多，现任检察官。」"}
        ]
        return EventResult("表示疑惑询问他是谁", 0, dialogue_sequence, past_story=get_past_story(favorability))

    elif choice == "2":
        logger.info("Player chose to nod and smile politely.")
        dialogue_sequence = [
            {"speaker": "你", "line": "你点头微笑，表示礼貌。"},
            {"speaker": "戈多", "line": "戈多微微一笑，「看来你还记得我。」"}
        ]
        return EventResult("点头微笑", 2, dialogue_sequence)

    elif choice == "3":
        logger.info("Player chose to directly refute.")
        dialogue_sequence = [
            {"speaker": "你", "line": "你毫不犹豫地反驳「这位先生，我不认识你。」"},
            {"speaker": "戈多", "line": "「哦？律师小姐，看来你贵人多忘事嘛……很好。」"}
        ]
        return EventResult("直接反驳", -3, dialogue_sequence)

    else：
        logger.warning(f"Unexpected choice '{choice}', defaulting to silence.")
        dialogue_sequence = [
            {"speaker": "你", "line": "你选择沉默不语。"},
            {"speaker": "戈多", "line": "戈多挑眉，似乎对你无言以对的操作感到意外。"},
        ]
        return EventResult("沉默", 0, dialogue_sequence)