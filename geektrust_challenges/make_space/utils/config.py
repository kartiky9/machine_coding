from models import TimeInterval, MeetingRoom

MEETING_ROOMS = [
    MeetingRoom('C-Cave', 3),
    MeetingRoom('D-Tower', 7),
    MeetingRoom('G-Mansion', 20),
]

BUFFER_TIMES = [
    TimeInterval('09:00', '09:15'),
    TimeInterval('13:15', '13:45'),
    TimeInterval('18:45', '19:00')
]
