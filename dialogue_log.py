
class DialogueLog:
    def __init__(self):
        self.logs = []
        
    def record_log_pool(self,result):
        log_pool = []
        
        #1.narrative
        if result.narrative:
            log_pool.append(f"Narrative: {result.narrative}")
            
        #2.玩家的选择和戈多的反应
        if result.player_choice and result.godot_reaction:
            log_pool.append(
                f"【玩家选择】：{result.player_choice}\n"
                f"【戈多的反应】：{result.godot_reaction}\n"
                f"【好感度变化】：{result.favor_change:+}\n"
            )
            
        #3.旁白小记
        if result.commentary:
            log_pool.append(f"旁白小记: {result.commentary}")
        
        #4.过去剧情
        if result.past_story:
            log_pool.append(f"过去剧情: {result.past_story}")
        
        full_log = "\n".join(log_pool)
        self.logs.append(full_log)
        
        def print_dialogue(self,final_favorability):
            print("---------------------------------------------------------------")
            print("\n【对话记录】")
            for log in self.logs:
                print(log)
            print("---------------------------------------------------------------")
            print(f"Final favorability: {final_favorability}")