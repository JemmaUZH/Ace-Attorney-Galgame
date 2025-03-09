import logging
from events.event_progress_1 import progress_1_event
from events.event_progress_2 import progress_2_event
from events.event_progress_3 import progress_3_event

logger = logging.getLogger(__name__)

class EventHandler:
    """
    事件处理器，根据游戏进度调用不同的事件逻辑。
    """

    def run_event(self, progress, likability):
        """
        运行当前进度的剧情事件。

        Args:
            progress (int): 当前游戏进度。
            likability (int): 当前角色好感度。

        Returns:
            EventResult: 事件结果，包含玩家选择的对话、好感度变化等信息。
        """
        if progress == 1:
            return progress_1_event(likability)
        elif progress == 2:
            return progress_2_event(likability)
        elif progress == 3:
            return progress_3_event(likability)
        else:
            logger.error(f"Invalid progress: {progress}")
            return None
