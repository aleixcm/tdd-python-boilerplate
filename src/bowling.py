from typing import Optional


class RollingException(Exception):
    pass


class Frame:
    def __init__(self):
        self.rolls: int = 2
        self.pins: int = 10
        self.score: int = 0
        self.is_strike: bool = False
        self.is_spare: bool = False

    def check_is_strike(self, pins_down: int) -> bool:
        if self.rolls == 2 and pins_down == self.pins:
            self.is_strike = True
            self.score = 10
            self.rolls = 0
            return True
        return False

    def roll(self, pins_down: Optional[int]) -> None:
        if pins_down is None:
            return None
        if self.rolls == 0:
            raise RollingException
        if pins_down > self.pins:
            raise RollingException
        if self.check_is_strike(pins_down):
            return None
        self.pins -= pins_down
        self.score += pins_down
        self.rolls -= 1
        if self.pins == 0:
            self.is_spare = True


class Bowling:
    def __init__(self):
        self.score: int = 0
        self.frames_num: int = 10
        self.last_frame: Optional[Frame] = None

    def get_score(self, frame: Frame) -> None:
        if self.last_frame:
            if self.last_frame.is_strike:
                self.score += frame.score
        self.score += frame.score

    def round(self, pins_down: tuple[int, int]) -> None:
        if self.frames_num == 0:
            raise RollingException
        self.frames_num -= 1
        frame = Frame()
        frame.roll(pins_down[0])
        frame.roll(pins_down[1])
        self.get_score(frame)
        self.last_frame = frame
