from config import character, initial_favorability
from dialogue_log import DialogueLog
from story_content import get_nickname
from events.event_progress_1 import progress_1_event
from events.event_progress_2 import progress_2_event
from events.event_progress_3 import progress_3_event

class StoryManager:
    def __init__(self):
        self.favorability = initial_favorability
        self.progress = 1
        self.dialogue_log = DialogueLog()
        
    def start_story(self):
        self.introduce_character()
        while self.progress <= 3:
            self.run_progress()
        self.dialogue_log.print_dialogue(self.favorability)
    
    def introduce_character(self):
        print("---------------------------------------------------------------")
        for key, value in character.items():
            print(f"{key}: {value}")
        print(f"「{get_nickname(self.favorability)}，好久不见。」")
        print(f"{character['name']}检察官微微一笑，目光却如同探针般刺入你的内心。\n")
        
    def run_progress(self):
        if self.progress == 1:
            result = progress_1_event(self.favorability)
        elif self.progress == 2:
            result = progress_2_event(self.favorability)
        else:
            result = progress_3_event(self.favorability)

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

        
        
                