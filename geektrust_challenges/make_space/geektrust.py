import sys

from models import TimeInterval
from utils.config import BUFFER_TIMES, MEETING_ROOMS
from services import MeetingScheduler, meeting_scheduler
from utils.exceptions import IncorrectInputError

from utils.constants import InputType, Output


class Driver:

    def __init__(self, scheduler: MeetingScheduler):
        self.scheduler = scheduler

    def process_line(self, line: str):
        line = line.strip()
        if line.startswith(InputType.BOOK):
            _, start, end, capacity = line.split()
            out = self.book_room(start, end, int(capacity))
            print(out)
        if line.startswith(InputType.VACANCY):
            _, start, end = line.split()
            out = self.vacancy(start, end)
            print(out)

    def book_room(self, start_time: str, end_time: str, capacity: int) -> str:
        try:
            time_interval = TimeInterval(start_time, end_time)
            room = self.scheduler.book_room(time_interval, capacity)
            if room:
                return room.name
            return Output.NO_VACANT_ROOM
        except IncorrectInputError:
            return Output.INCORRECT_INPUT

    def vacancy(self, start_time: str, end_time: str) -> str:
        try:
            time_interval = TimeInterval(start_time, end_time)
            room_list = self.scheduler.get_vacancies(time_interval)
            if room_list:
                return " ".join([room.name for room in room_list])
            return Output.NO_VACANT_ROOM
        except IncorrectInputError:
            return Output.INCORRECT_INPUT


def main():
    input_file = sys.argv[1]

    scheduler = MeetingScheduler(MEETING_ROOMS, BUFFER_TIMES)
    driver = Driver(scheduler)

    with open(input_file, 'r+') as f:
        for line in f.readlines():
            driver.process_line(line)


if __name__ == "__main__":
    main()
