
from typing import List, Optional
from models import MeetingRoom, TimeInterval


class MeetingScheduler:

    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance and isinstance(cls._instance, MeetingScheduler):
            return cls._instance
        else:
            raise Exception("Instance not created")

    @classmethod
    def create_instance(cls, meeting_rooms: List[MeetingRoom], buffer_times: List[TimeInterval]):
        if not cls._instance:
            cls._instance = MeetingScheduler(
                meeting_rooms, buffer_times)
        return cls._instance

    def __init__(self, meeting_rooms: List[MeetingRoom], buffer_times: List[TimeInterval]) -> None:
        self.meeting_rooms = meeting_rooms
        self.buffer_times = buffer_times

    def book_room(self, time_interval: TimeInterval, capacity: int) -> Optional[MeetingRoom]:
        if self._check_overlap_with_buffer(time_interval):
            return None

        for room in self.meeting_rooms:
            if room.capacity >= capacity and self._is_room_available(room, time_interval):
                self._book_room(room, time_interval)
                return room

    def get_vacancies(self, time_interval: TimeInterval) -> List[MeetingRoom]:
        vacancy_list = []
        if self._check_overlap_with_buffer(time_interval):
            return vacancy_list
        for room in self.meeting_rooms:
            if self._is_room_available(room, time_interval):
                vacancy_list.append(room)
        return vacancy_list

    def _book_room(self, room: MeetingRoom, time_interval: TimeInterval):
        room.scheduled_meetings.append(time_interval)
        room.scheduled_meetings.sort(key=lambda interval: interval.start_time)

    def _is_room_available(self, room: MeetingRoom, time_interval: TimeInterval) -> bool:
        for interval in room.scheduled_meetings:
            if interval.check_overlap(time_interval):
                return False
        return True

    def _check_overlap_with_buffer(self, time_interval: TimeInterval) -> bool:
        for interval in self.buffer_times:
            if interval.check_overlap(time_interval):
                return True

        return False
