import logging
from config import character, initial_favorability, logger
from dialogue_log import DialogueLog
from story_content import get_nickname
from events.event_progress_1 import progress_1_event
from events.event_progress_2 import progress_2_event
from events.event_progress_3 import progress_3_event

logger = logging.getLogger(__name__)

class StoryManager:
    """
    故事管理器，负责整个故事的流程控制
    """
    def __init__(self):
        self.favorability = initial_favorability
        self.progress = 1
        self.dialogue_log = DialogueLog()
        logger.info("Story Manager initialized.")
        
    def start_story(self):
        """
        启动故事流程，依次运行剧情时间
        """
        logger.info("Story started.")
        self.introduce_character()
        while self.progress <= 3:
            self.run_progress()
        self.dialogue_log.print_dialogue(self.favorability)
        logger.info("Story ended.")
    
    def introduce_character(self):
        """
        介绍人物，打印人物档案和开场白
        """
        print("---------------------------------------------------------------")
        print("【人物档案】\n")
        for key, value in character.items():
            print(f"{key}：{value}")
        print("\n---------------------------------------------------------------\n")

        print("「猫咪小姐，好久不见。」\n")
        print(f"{character['姓名']}检察官微微一笑，目光却如同探针般刺入你的内心。\n")

        print("---------------------------------------------------------------")
        print("【选项】")
        print("1. 表示疑惑")
        print("2. 点头微笑")
        print("3. 直接反驳")

        
    def run_progress(self):
        """
        运行剧情进程，根据进度调用不同的事件处理函数
        """
        
        if self.progress == 1:
            result = progress_1_event(self.favorability)
        elif self.progress == 2:
            result = progress_2_event(self.favorability)
        else:
            result = progress_3_event(self.favorability)
            
        # 如果有过去剧情，先打印过去剧情
        if result.past_story:
            print("\n【过去剧情】")
            print(result.past_story)
            print()

        # 每条对话正常打印
        for entry in result.dialogue_sequence:
            if entry["speaker"] == "Narrator":
                print(entry["line"])
            else:
                print(entry["line"])  # 不要额外加角色名，保证台词自然

        # 加一个空行，作为Progress之间的分隔
        print("---------------------------------------------------------------")

        self.favorability += result.favor_change
        self.dialogue_log.record_log_pool(result)
        self.progress += 1

        
        
                