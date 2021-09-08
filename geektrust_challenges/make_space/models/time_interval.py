from __future__ import annotations

from .time import Time

from utils.exceptions import IncorrectInputError


class TimeInterval:

    def __init__(self, start_time: str, end_time: str) -> None:
        self.start_time = Time(start_time)
        self.end_time = Time(end_time)
        self.validate_time_interval()

    def validate_time_interval(self):
        if self.end_time <= self.start_time:
            raise IncorrectInputError(
                f"End Time: {self.end_time} cannot be less than Start Time: {self.start_time}")

    def check_overlap(self, other: TimeInterval):
        return (self.start_time < other.end_time <= self.end_time) or (self.start_time <= other.start_time < self.end_time)

    def __str__(self) -> str:
        return f"Start: {self.start_time}, End: {self.end_time}"
