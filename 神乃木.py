import random

# 角色信息
character = {
    "name": "戈多",
    "age": 27,
    "occupation": "检察官",
    "personality": "温文尔雅，礼貌周到，但每句话都带着隐含的试探和压迫感",
    "background": "神秘的检察官，五年前与你有一面之缘",
    "mood": "温柔中带着试探",
    "signature_move": "用温柔的语气说出最让人窒息的话"
}

# 全局好感度
favorability = 60

# 存储剧情的对话日志列表
dialogue = []

# 旁白小记（吐槽）
旁白小记 = [
    "——旁白小记：对方的微笑比黑咖啡还苦，看来今天这杯对话不会太甜。",
    "——旁白小记：标准“熟人套近乎”，但熟到让人背后发凉那种。",
    "——旁白小记：笑容越温柔，越像刀子上抹蜜……老套路了。",
    "——旁白小记：刚见面就甩这种台词，果然是个自带BGM的男人。",
    "——旁白小记：脸上的笑容写着‘我什么都知道’，但他到底知道多少？"
]

# 根据好感度动态生成称呼
def get_nickname():
    if favorability >= 60:
        return "猫咪小姐"
    elif favorability <= 40:
        return "女士"
    else:
        return "被告小姐"

# 戈多登场介绍
def introduce_character():
    print("---------------------------------------------------------------")
    print(f"【{character['name']}】")
    print(f"年龄：{character['age']}岁")
    print(f"职业：{character['occupation']}")
    print(f"性格：{character['personality']}")
    print(f"背景故事：{character['background']}")
    print(f"当前表情：{character['mood']}")
    print("---------------------------------------------------------------\n")
    print(f"「{get_nickname()}，好久不见。」")
    print(f"{character['name']}检察官微微一笑，目光却如同探针般刺入你的内心。\n")

# 记录每次对话
def record_dialogue(player_choice, godot_reaction, favor_change, key_note=None, past_story_text=None):
    review = random.choice(旁白小记)
    log = (
        f"玩家选择：{player_choice}\n"
        f"戈多的反应：{godot_reaction}\n"
        f"{review}\n"
        f"好感度变化：{favor_change:+}\n"
    )
    if past_story_text:
        log += f"\n{past_story_text}\n"
    dialogue.append(log)

#新增剧情轮次
progress = 1

# 玩家选择分支
def player_choice():
    global progress
    if progress == 1:
        handle_progress_1()
    elif progress == 2:
        handle_progress_2()
    elif progress == 3:
        handle_progress_3()

def handle_progress_1():
    global favorability, progress
    player_choice_text = "未知选项"  # 默认初始化，防止漏掉
    reaction = ""
    favor_change = 0
    past_story_text = None
    
    print("【选项】")
    print("1. 表示疑惑询问他是谁")
    print("2. 点头微笑")
    print("3. 直接反驳")
    
    choice = input("输入选项编号(1-3)：")

    if choice == "1":
        player_choice_text = "表示疑惑询问他是谁"
        reaction = "举起咖啡轻酌，「才五年过去，你已经把我给忘了吗？我是戈多，现任检察官。」"
        print("\n你的脸上露出疑惑的神情：「这位先生，请问你是？」")
        print(f'{character["name"]}: {reaction}')
        past_story_text = past_story()
        favor_change = 0
    elif choice == "2":
        player_choice_text = "点头微笑"
        reaction = "微微一笑，「看来你还记得我。」"
        print("\n你点头微笑，表示礼貌。")
        print(f'{character["name"]}: {reaction}')
        favor_change = +2
        past_story_text = None
    elif choice == "3":
        player_choice_text = "直接反驳"
        reaction = "「哦？律师小姐，看来你贵人多忘事嘛……很好。」"
        print("\n你毫不犹豫地反驳：「这位先生，我不认识你。」")
        print(f'{character["name"]}: {reaction}')
        favor_change = -3
        past_story_text = None
    else:
        player_choice_text = "什么都不说"
        reaction = "「什么都不说？真是有趣呢，猫咪小姐。」"
        print("\n戈多挑眉，似乎对你无言以对的操作感到意外。\n")
        print(f"{character['name']}：{reaction}")
        favor_change = 0
        past_story_text = None
    
    #更新好感度和进度
    favorability += favor_change
    progress += 1
    
    
    # 记录对话
    record_dialogue(player_choice_text, reaction, favor_change, past_story_text)
    print(f"（隐藏好感度：{favorability})\n")
    print("---------------------------------------------------------------")
    
def handle_progress_2():
    global favorability, progress
    player_choice_text = "未知选项"  # 默认初始化，防止漏掉
    reaction = ""
    favor_change = 0
    past_story_text = None
        
    print(f"\n{character['name']}：「无论如何，{get_nickname()}，现在你还是头疼一下你的被告人吧，我可真羡慕他，闯出这么大的祸还要你为他收拾。」")
    print("【选项】")
    print("1. 他是无罪的")
    print("2. 这与你无关")
    print("3. 是啊，他真的是很麻烦")
    
    choice = input("输入选项编号(1-3)：")

    if choice == "1":
        player_choice_text = "他是无罪的"
        reaction = (
            f"轻笑，「真是难得，{get_nickname()}，这么多年不见，你还是这么天真。"
            "你这么相信他，是因为律师的虚张声势，还是只是因为...」"
            "他身子前俯，话语却还带一丝玩味，「他是你的男朋友呢？」"
        )
        print("\n「他是无罪的，我会证明给你看。」")
        print(f'{character["name"]}: {reaction}')
        favor_change = 0
    elif choice == "2":
        player_choice_text = "这与你无关"
        reaction = """脸上的笑容消失了，「律师小姐，我从地狱爬出来，就是为了今天，可以站在这里。」
        虽然你看不到他脸上的表情，但你能感受到他在看着你。
        「怎么会与我无关呢……那就一会儿让我见识一下这个与你有关的男朋友吧。」"""
        print("\n「这件事和你无关，检察官先生，我只想保护他。」")
        print(f'{character["name"]}: {reaction}')
        favor_change = -3
        past_story_text = None
    elif choice == "3":
        player_choice_text = "是啊，他真的是很麻烦"
        reaction = "喝咖啡的手一顿，沉默了片刻，「啧，我什么时候让你彻夜失眠了？你这样说的，让我以为你对你的新男朋友已经毫无感情了呢。」"
        print("\n你扶额：「是啊，他真的是很麻烦，如果不是因为我相信他的人品，我才不接手这个案件呢。不过至少比起你，他还没让我彻夜失眠。」")
        print(f'{character["name"]}: {reaction}')
        favor_change = +5
        past_story_text = None
    else:
        player_choice_text = "什么都不说"
        reaction = "「怎么了，是还在烦恼你新男朋友的案件吗？」"
        print(f"{character['name']}：{reaction}")
        favor_change = 0
        past_story_text = None
    
    #更新好感度和进度
    favorability += favor_change
    progress += 1
    
    record_dialogue(player_choice_text, reaction, favor_change, past_story_text)
    print(f"（隐藏好感度：{favorability})\n")
    print("---------------------------------------------------------------")

def handle_progress_3():
    global favorability, progress
    player_choice_text = "未知选项"  # 默认初始化，防止漏掉
    reaction = ""
    favor_change = 0
    past_story_text = None
    
    if favorability > 65:
        print("「什么男朋友！我可没喜欢过这家伙！」")
    elif favorability < 55:
        print("\n「男朋友？你满脑子只有情爱吗？我是他的律师，仅此而已。」")
    else:
        print("\n「你误会了，他才不是我男朋友。」")
    favor_change = +1
    
    print("\n【选项】")
    print("1. 冷静分析证据")
    print("2. 问戈多为什么突然回来")
    print("3. 坚定维护委托人，直接反击")
    
    choice = input("输入选项编号(1-3)：")
    
    if choice == "1":
        player_choice_text = "冷静分析证据"
        print("\n你抽出案件的文案，给戈多看并分析。")
        if favorability > 65:
            reaction = f"{character['name']}微微一笑：「果然，你还是那个我认识的猫咪小姐。」"
            favor_change = +2
            key_note = "玩家主动分析证据，态度理性"
        elif favorability < 55:
            reaction = f"{character['name']}冷笑：「现在才装冷静，有点晚了吧？」"
            favor_change = 0
            key_note = "玩家被动分析证据，缺乏信任感"
        else:
            reaction = f"{character['name']}点头：「听听你的分析吧。」"
            favor_change = +1
            key_note = "玩家正常分析证据"
    
    elif choice == "2":
        player_choice_text = "质问戈多的执着"
        if favorability > 65:
            reaction = f"{character['name']}把咖啡一饮而尽：「有些真相，我只想从你口中听到。」"
            favor_change = +1
            key_note = "玩家询问戈多，戈多坦白动机"
        elif favorability < 55:
            reaction = f"{character['name']}：「呵。」"
            favor_change = -1
            key_note = "玩家询问失败，戈多态度强硬"
        else:
            reaction = f""""{character['name']}：「...咖啡之苦，非是对味蕾的惩罚，而是对心灵的邀请。
            它领你走入暮色中的玫瑰园，
            听潮水在远方低声吟诵逝去的誓言，
            直到你明白，世间万物都曾以苦为名，学会生长。」
            """
            favor_change = 0
            key_note = "玩家询问戈多，但未获取有效信息"
    
    elif choice == "3":
        player_choice_text = "坚定维护委托人"
        reaction = f"{character['name']}微微摇头：「所以，你终究还是站在他那边啊...」"
        favor_change = 0
        key_note = "玩家明确立场，戈多有点失落"
        
    else:
        player_choice_text = "沉默不语"
        reaction = f"{character['name']}：「沉默不代表无罪，{get_nickname()}。」"
        favor_change = 0
        key_note = "玩家保持沉默，戈多态度难测"
    
    #更新好感度和进度
    favorability += favor_change
    progress += 1
    
    # 输出对话和反应
    print(f"\n{player_choice_text}\n")
    print(f"\n{reaction}\n")
    print(f"（隐藏好感度：{favorability}）\n")

    # 记录对话
    record_dialogue(player_choice_text, reaction, favor_change, key_note)
        
        

# 叙旧剧情（返回文本）
def past_story():
    parts = [
        "——【五年前的回忆】",
        "戈多低头看着杯中苦涩漆黑的液体，仿佛陷入某种回忆。",
        "「那是五年前……你还记得那场离奇的案件吗？」",
        "「无名尸体、消失的证据、以及……你最后留下的那句‘异议’，我可一直记得。」"
    ]
    if favorability > 50:
        parts.extend([
            "他抬起眼，微微一笑，眼底似乎透出一丝怀念。",
            "「说实话……再次见到你，我其实有点开心。」",
            "但是你观察到，他的微笑中透着薄薄的寒意。",
            "「只可惜，当年的你，现在已经站在我的对立面了吧？」\n"
        ])
    else:
        parts.extend([
            "戈多轻叹一口气，微微摇头。",
            "「果然，你已经把过去的一切都抛诸脑后了吗……」"
        ])
    for line in parts:
        print(line)
    return "\n".join(parts)

# 最终打印日志
def print_dialogue():
    print("---------------------------------------------------------------")
    print("\n【对话记录】")
    for log in dialogue:
        print(log)
    print(f"（最终好感度：{favorability}）\n")

def main():
    global progress
    
    introduce_character()
    while progress <= 3:
        player_choice()
    
    print_dialogue()

if __name__ == "__main__":
    main()
