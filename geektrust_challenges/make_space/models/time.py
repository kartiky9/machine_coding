from __future__ import annotations

from typing import Tuple

from utils.constants import MINUTE_INTERVALS

from utils.exceptions import IncorrectInputError


class Time:
    def __init__(self, time_string: str) -> None:
        hours, minutes = self._get_hours_and_minutes(time_string)
        self.hours = hours
        self.minutes = minutes

    def _get_hours_and_minutes(self, time_string: str) -> Tuple[int, int]:
        hours, minutes = self._split_time_string(time_string)
        try:
            hours = int(hours)
            minutes = int(minutes)
        except ValueError:
            raise IncorrectInputError(f"Invalid time_string: {time_string}")
        return hours, minutes

    def _split_time_string(self, time_string: str):
        if len(time_string) != 5 or ":" not in time_string:
            raise IncorrectInputError(f"Invalid time_string: {time_string}")
        return time_string.split(":")

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, value):
        if not (0 <= value < 24):
            raise IncorrectInputError(
                f"Hours: {value} should be in range (0, 24)")
        self._hours = value

    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, value):
        if not (0 <= value < 60 and value % MINUTE_INTERVALS == 0):
            raise IncorrectInputError(
                f"Minutes: {value} should be in range(0, 60) and in multiples of 15")
        self._minutes = value

    def __gt__(self, other: Time):
        return (self.hours > other.hours or (self.hours == other.hours and self.minutes > other.minutes))

    def __eq__(self, other: Time):
        return (self.hours == other.hours and self.minutes == other.minutes)

    def __ge__(self, other: Time):
        return (self.__eq__(other) or self.__gt__(other))

    def __lt__(self, other: Time):
        return not self.__ge__(other)

    def __le__(self, other: Time):
        return not self.__gt__(other)

    def __ne__(self, other: Time) -> bool:
        return not self.__eq__(other)

    def __str__(self) -> str:
        hours = '0'+str(self.hours) if self.hours < 10 else self.hours
        minutes = '0'+str(self.minutes) if self.minutes < 10 else self.minutes
        return f"{hours}:{minutes}"
