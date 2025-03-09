# **逆转裁判Galgame - 交互式剧情游戏框架**

## 📖 **项目简介**
**逆转裁判-Galgame** 是一个交互式剧情游戏框架，允许玩家在文本对话中做出选择，影响剧情发展与角色关系。游戏围绕核心角色 **戈多** 展开，玩家的选择将影响对话内容、角色好感度（likability）以及剧情走向。

本项目采用 **Python** 进行开发，并使用 **JSON** 进行数据存储，同时支持未来扩展至 **SQLite** 以支持更复杂的数据管理。

---

## 🔧 **项目结构**
```
30days/
│── main.py                  # 入口文件，启动游戏
│── config.py                # 配置文件，存储全局参数
│── story_manager.py         # 故事管理器，控制游戏流程
│── event_handler.py         # 事件管理器，处理不同的剧情进展
│── game_state.py            # 游戏状态管理，存储好感度、进度等信息
│── dialogue_log.py          # 对话记录系统
│── events/                  # 事件处理模块
│   │── event_progress_1.py  # 第一阶段剧情事件
│   │── event_progress_2.py  # 第二阶段剧情事件
│   │── event_progress_3.py  # 第三阶段剧情事件
│── story_content.py         # 固定剧情文本，如背景故事、角色信息
│── utils/                   # 辅助工具模块
│── tests/                   # 测试用例
│── README.md                # 说明文档
```

---

## 🚀 **安装与运行**

### **1️⃣ 安装环境**
确保系统已安装 **Python 3.8+**，然后创建并激活虚拟环境：
```bash
python -m venv .venv
source .venv/bin/activate  # MacOS/Linux
.venv\Scripts\activate    # Windows
```

### **2️⃣ 安装依赖**
```bash
pip install -r requirements.txt
```

### **3️⃣ 运行游戏**
```bash
python main.py
```

---

## 🎮 **游戏玩法**
- 游戏以文本对话的方式进行，玩家可选择不同选项，影响剧情发展。
- 角色 **戈多** 会根据玩家的对话历史、好感度等动态调整反应。
- 游戏状态（如 **好感度 likability**）会影响角色称呼、语气和故事结局。

示例：
```
「猫咪小姐，好久不见。」

【选项】
1. 表示疑惑
2. 点头微笑
3. 直接反驳

输入选项编号(1-3)：
```

---

## 🔬 **技术实现**
### **✨ 主要功能**
- **事件驱动的游戏进程**：使用 `EventHandler` 处理不同剧情节点。
- **动态好感度系统**：`GameState` 记录玩家选择并实时调整好感度。
- **对话日志管理**：`DialogueLog` 记录游戏中的所有对话和事件。
- **可扩展的存储系统**：目前采用 **JSON** 存储，未来可扩展至 **SQLite**。
- **日志与调试支持**：使用 `logging` 记录游戏运行情况，便于调试。

---

## ✅ **未来改进计划**
- [ ] **增加多角色互动**，扩展除 **戈多** 以外的可攻略角色。
- [ ] **优化 AI 角色对话逻辑**，基于历史对话增强 NPC 反应。
- [ ] **加入存档功能**，允许玩家保存/读取游戏进度。
- [ ] **支持 GUI 界面**，提供更直观的用户交互体验。
- [ ] **扩展游戏事件系统**，允许复杂剧情分支。

---

## 👥 **贡献 & 反馈**
欢迎提交 **Issue** 或 **Pull Request**！
如果你有任何建议或发现 Bug，请在 GitHub 上提交 Issue，让我们一起优化这个项目！ 🎉

