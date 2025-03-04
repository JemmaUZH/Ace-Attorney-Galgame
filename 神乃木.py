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
def record_dialogue(player_choice, godot_reaction, favor_change, past_story_text=None):
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

# 玩家选择分支
def player_choice():
    global favorability
    
    print('【选项】')
    print('1. 表示疑惑询问他是谁')
    print('2. 点头微笑')
    print('3. 直接反驳')

    choice = input('输入选项编号(1-3)：')

    if choice == "1":
        player_choice_text = "表示疑惑询问他是谁"
        reaction = "举起咖啡轻酌，「才五年过去，你已经把我给忘了吗？我是戈多，现任检察官。」"
        print("\n你的脸上露出疑惑的神情：「这位先生，请问你是？」")
        print(f'{character["name"]}: {reaction}')
        past_story_text = past_story()
        favor_change = 0

    elif choice == "2":
        player_choice_text = "点头微笑"
        reaction = "戈多微微一笑，「看来你还记得我。」"
        print("\n你点头微笑，表示礼貌。")
        print(f'{character["name"]}: {reaction}')
        favorability += 2
        favor_change = +2
        past_story_text = None

    elif choice == "3":
        player_choice_text = "直接反驳"
        reaction = "「哦？律师小姐，看来你贵人多忘事嘛……很好。」"
        print("\n你毫不犹豫地反驳：「这位先生，我不认识你。」")
        print(f'{character["name"]}: {reaction}')
        favorability -= 2
        favor_change = -2
        past_story_text = None

    else:
        player_choice_text = "什么都不说"
        reaction = "「什么都不说？真是有趣呢，猫咪小姐。」"
        print("\n戈多挑眉，似乎对你无言以对的操作感到意外。\n")
        print(f"{character['name']}：{reaction}")
        favor_change = 0
        past_story_text = None

    # 记录对话
    record_dialogue(player_choice_text, reaction, favor_change, past_story_text)

    print(f"（隐藏好感度：{favorability})\n")

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
            "「说实话……再次见到你，我其实有点开心。」"
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
    introduce_character()
    player_choice()
    print_dialogue()

if __name__ == "__main__":
    main()
