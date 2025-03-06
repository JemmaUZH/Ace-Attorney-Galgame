def get_nickname(favorability):
    if favorability >= 60:
        return "猫咪小姐"
    elif favorability <= 40:
        return "女士"
    else:
        return "被告小姐"

def get_past_story(favorability):
    parts = [
        "——【五年前的回忆】",
        "戈多低头看着杯中苦涩漆黑的液体，仿佛陷入某种回忆。",
        "「那是五年前……你还记得那场离奇的案件吗？」",
        "「无名尸体、消失的证据、以及……你最后留下的那句‘异议’，我可一直记得。」"
    ]
    
    if favorability > 50:
        parts.extend([
            "他抬起眼，微微一笑，眼底似乎透出一丝你读不懂的情绪。",
            "「真的是很久了呢。」","
        ])
    else:
        parts.extend([
            "戈多轻叹一口气，微微摇头。",
            "「果然，你已经把过去的一切都抛诸脑后了吗……」"
        ])
    
    return "\n".join(parts)
    
