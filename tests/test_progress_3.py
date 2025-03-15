import pytest
from unittest.mock import patch
from events.event_progress_3 import EventResult, sanitize_input, progress_3_event  
from story_content import get_nickname

@pytest.mark.parametrize("likability, expected_choice, expected_favor_change", [
    (70, "冷静分析证据", 2),   # 高好感度 → +2
    (50, "冷静分析证据", 1),   # 中等好感度 → +1
    (40, "冷静分析证据", 0),   # 低好感度 → 0
])
def test_progress_3_analyze_evidence(mocker, likability, expected_choice, expected_favor_change):
    """
    测试玩家选择【冷静分析证据】时的输出。
    """
    mocker.patch("builtins.input", return_value="1")  # 模拟用户输入 "1"

    result = progress_3_event(likability)

    assert isinstance(result, EventResult)
    assert result.player_choice == expected_choice
    assert result.favor_change == expected_favor_change
    assert len(result.dialogue_sequence) > 0  # 确保对话有内容


@pytest.mark.parametrize("likability, expected_choice, expected_favor_change", [
    (70, "质问戈多的执着", 1),
    (50, "质问戈多的执着", 0),
    (40, "质问戈多的执着", -1),
])
def test_progress_3_question_godot(mocker, likability, expected_choice, expected_favor_change):
    """
    测试玩家选择【质问戈多为什么回来】时的输出。
    """
    mocker.patch("builtins.input", return_value="2")  # 模拟输入 "2"

    result = progress_3_event(likability)

    assert isinstance(result, EventResult)
    assert result.player_choice == expected_choice
    assert result.favor_change == expected_favor_change


@pytest.mark.parametrize("likability", [70, 50, 40])
def test_progress_3_defend_client(mocker, likability):
    """
    测试玩家选择【坚定维护委托人】时的输出。
    """
    mocker.patch("builtins.input", return_value="3")  # 模拟输入 "3"

    result = progress_3_event(likability)

    assert isinstance(result, EventResult)
    assert result.player_choice == "坚定维护委托人"
    assert result.favor_change == 0


def test_progress_3_invalid_input(mocker):
    """
    测试无效输入（比如输入 "abc"）时是否默认进入沉默选项。
    """
    mocker.patch("builtins.input", return_value="invalid")  # 模拟输入 "invalid"

    result = progress_3_event(50)

    assert isinstance(result, EventResult)
    assert result.player_choice == "沉默"
    assert result.favor_change == 0
    assert len(result.dialogue_sequence) > 0
