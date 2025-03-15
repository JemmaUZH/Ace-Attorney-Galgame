import pytest
from unittest.mock import patch
from events.event_progress_1 import EventResult, sanitize_input, progress_1_event
from story_content import get_past_story


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
        ("1", "表示疑惑询问他是谁", 0),
        ("2", "点头微笑", 2),
        ("3", "直接反驳", -3),
        ("x", "沉默", 0),
    ],
)
def test_progress_1_event(choice, expected_choice, expected_favor_change):
    likability = 50  # 测试用默认值
    past_story = "过去的故事内容"  # 假设 `get_past_story` 返回的内容
    with patch("builtins.input", return_value=choice), patch("story_content.get_past_story", return_value=past_story):
        result = progress_1_event(likability)

    assert isinstance(result, EventResult)
    assert result.player_choice == expected_choice
    assert result.favor_change == expected_favor_change

    if likability < 60:
        assert result.past_story == past_story
    else:
        assert result.past_story is None

