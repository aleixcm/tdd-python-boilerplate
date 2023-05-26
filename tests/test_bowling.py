import pytest

from src.bowling import Bowling, Frame, RollingException


def test_bowling_score_return_0_at_start():
    bowling = Bowling()
    assert bowling.score == 0


def test_frame_roll_is_strike():
    frame = Frame()
    frame.roll(10)
    assert frame.is_strike is True
    assert frame.score == 10
    assert frame.rolls == 0


def test_frame_roll_is_spare():
    frame = Frame()
    frame.roll(2)
    frame.roll(8)
    assert frame.is_spare is True
    assert frame.score == 10
    assert frame.rolls == 0


def test_bowling_cant_roll_more_10_pins():
    frame = Frame()
    with pytest.raises(RollingException):
        frame.roll(11)


def test_frame_cant_roll_more_10_pins_in_two_rolls():
    frame = Frame()
    frame.roll(2)
    with pytest.raises(RollingException):
        frame.roll(9)


def test_frame_cant_roll_more_than_two_times():
    frame = Frame()
    frame.roll(3)
    frame.roll(5)
    with pytest.raises(RollingException):
        frame.roll(1)


def test_bowling_cant_roll_more_10():
    bowling = Bowling()
    for _ in range(10):
        bowling.round((3, 4))
    with pytest.raises(RollingException):
        bowling.round((4, 5))


def test_bowling_total_score():
    bowling = Bowling()
    bowling.round((3, 4))
    bowling.round((4, 5))
    assert bowling.score == 16


def test_bowling_total_score_with_strike():
    bowling = Bowling()
    bowling.round((3, 4))
    bowling.round((10, None))
    bowling.round((4, 5))
    assert bowling.score == 35
