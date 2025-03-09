import pytest
from unittest.mock import patch
from your_module_name import EventResult, sanitize_input, progress_2_event  # 替换 your_module_name
from story_content import get_nickname

@pytest.mark.parametrize(
    "user_input, valid_choices, expected",
    [
        ("1", ["1", "2", "3"], "1"),
        (" 2 ", ["1", "2", "3"], "2"),  # 测试去除空格
        ("4", ["1", "2", "3"], "invalid"),  # 无效选项
        ("hello", ["1", "2", "3"], "invalid"),  # 非数字输入
    ],
)
def test_sanitize_input(user_input, valid_choices, expected):
    assert sanitize_input(user_input, valid_choices) == expected

@pytest.mark.parametrize(
    "choice, expected_choice, expected_favor_change",
    [
        ("1", "他是无罪的", 0),
        ("2", "这与你无关", -3),
        ("3", "是啊，他真的是很麻烦", 5),
        ("x", "沉默", 0),
    ],
)
def test_progress_2_event(choice, expected_choice, expected_favor_change):
    favorability = 50  # 测试用默认值
    nickname = "小猫咪"  # 假设 `get_nickname` 返回的值
    with patch("builtins.input", return_value=choice), patch("story_content.get_nickname", return_value=nickname):
        result = progress_2_event(favorability)

    assert isinstance(result, EventResult)
    assert result.player_choice == expected_choice
    assert result.favor_change == expected_favor_change

    # 确保对话序列不为空
    assert result.dialogue_sequence
    assert any("戈多" in dialogue["speaker"] for dialogue in result.dialogue_sequence)
