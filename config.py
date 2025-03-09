import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,  # 记录INFO级别以上的日志
    format="%(asctime)s - %(levelname)s - %(message)s",  # 日志格式
    datefmt="%Y-%m-%d %H:%M:%S",  # 时间格式
    handlers=[
        logging.FileHandler("logs.txt", encoding="utf-8"),  # 日志写入 logs.txt 文件
        logging.StreamHandler()  # 也在控制台显示
    ]
)

logger = logging.getLogger(__name__)  # 获取日志对象


character = {
    "姓名": "戈多",
    "年龄": 27,
    "职业": "检察官",
    "性格": "温文尔雅，礼貌周到，但每句话都带着隐含的试探和压迫感",
    "背景": "神秘的检察官，五年前与你有一面之缘",
    "情绪": "温柔中带着试探",
    "惯用招数": "用温柔的语气说出最让人窒息的话"
}

initial_likability = 60
progress = 1

narration_notes = [
    # 通用压迫感
    "对方的微笑比黑咖啡还苦，看来今天这杯对话不会太甜。",
    "标准的“熟人寒暄”，但熟到让人后背发凉的那种。",
    "笑容越温柔，越像刀子上抹蜜……熟悉的压迫感回来了。",
    "刚见面就甩这种台词，果然是个自带BGM的男人。",
    "脸上的笑容写着“我什么都知道”，但他到底知道多少？",
    "咖啡香气里裹着看不见的火药味，笑容是引信。",
    "每句话都温柔得像情诗，但每个字都藏着刀锋。",
    "你能感觉到，他的目光像是穿透你伪装的X光机。",
    "这场对话从开始就没有退路，你只是看似坐在谈判桌前。",
    "他的话像是一张网，每一句都在慢慢收紧。",
    "表面礼貌寒暄，骨子里却是审问庭的攻防战。",
    "空气里飘着咖啡香，但比咖啡更苦的是他每一句话。",
    "这场谈话，就像在刀尖上跳舞，退无可退。",
    "五年的距离，并没有冲淡他对你的兴趣，反而更加锋利。",
    "他知道你的答案，但还是想亲口听你说出来。",
    "每一个笑容都像诱饵，等着你自己跳进去。",

    # 特定场合1：久别重逢感
    "五年不见，熟悉又陌生，他的微笑像老照片里褪色的阳光。",
    "时间没能带走他身上的那股锐利，只是让它更加隐蔽。",
    "久别重逢，他的话语依旧温柔，却更像是慢慢勒紧的绳索。",
    "再见面，他没问过得好吗，因为他知道，这种问候对彼此都太奢侈。",
    "五年时光，他变了，但那种让人透不过气的存在感，一点没变。",

    # 特定场合2：审问对峙感
    "你坐在椅子上，感觉自己像证人席上的被告。",
    "无形的审问已经开始，每个问题都藏着陷阱。",
    "没有审讯灯，却比审讯室还让人发冷。",
    "他的目光像搜索灯，每一寸迟疑都无所遁形。",
    "你知道他说的每个字都有伏笔，等着你自己踩进去。",
    "这不是普通的对话，而是一场无声的攻防战。",
    "表面上是谈话，实际上是无声的对峙，每个眼神都是试探。",

    # 特定场合3：个人情感暗涌
    "温柔的目光背后，藏着五年未曾说出口的心事。",
    "他的话题绕了一圈，却总是不小心回到你们之间。",
    "就像杯中的咖啡，苦的是回忆，烫的是沉默。",
    "他问的每个问题，似乎都带着某种私人期待。",
    "话到一半，眼神却泄露了五年前没说完的话。"
]