import logging
from config import logger, initial_likability
from dialogue_log import DialogueLog
from event_handler import EventHandler
from game_state import GameState

logger = logging.getLogger(__name__)

class StoryManager:
    """
    故事管理器，负责整个故事的流程控制
    """
    def __init__(self):
        """
        初始化StoryManager, 家在游戏状态和对话日志
        """
        self.game_state = GameState(initial_likability)
        self.dialogue_log = DialogueLog()
        self.event_handler = EventHandler()
        
        logger.info("Story Manager initialized.")
        
    def start_story(self):
        """
        启动故事流程，依次运行剧情时间
        """
        logger.info("Story started.")
        self.game_state.introduce_character()
        
        while self.game_state.progress <= 3:
            self.run_progress()

        self.dialogue_log.print_dialogue(self.game_state.likability)
        logger.info("Story ended.")
        
    def run_progress(self):
        """
        运行剧情进程，根据进度调用不同的事件处理函数
        """
        
        result = self.event_handler.run_event(self.game_state.progress, self.game_state.likability)
        
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
        self.game_state.update_state(result)
        self.dialogue_log.record_log_pool(result)

        
        
                