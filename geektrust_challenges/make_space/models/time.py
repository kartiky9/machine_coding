from dataclasses import dataclass

from exceptions import IncorrectInputError

class Time:
    def __init__(self, time_string: str) -> None:
        pass


    def _get_hours_and_minutes(self, time_string):
        if len(time_string) > 5 and ":" not in time_string:
            raise IncorrectInputError(f"Invalid time_string: {time_string}")
        hours, minutes = time_string.split(":")