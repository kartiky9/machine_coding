from dataclasses import dataclass, field
from .time_interval import TimeInterval
from typing import List


@dataclass
class Room:
    name: str
    capacity: int


@dataclass
class MeetingRoom(Room):
    scheduled_meetings: List[TimeInterval] = field(default_factory=list)
