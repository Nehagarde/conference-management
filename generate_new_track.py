"""Generate New Track Here. New Track=New Day"""

import datetime

class NewTrack:
    """This Class has function to initialize a new track
    """
    def __init__(self):
        self.MORNING_TIME_LIMIT = 180
        self.NOON_TIME_LIMIT = 240
        self.morning_start_time = datetime.datetime.strptime("9:00", '%H:%M')
        self.noon_start_time = datetime.datetime.strptime("1:00", '%H:%M')
        self.total_morning_time = 0
        self.total_noon_time = 0
        self.is_set_lunch = False
        self.morning_session_list = []
        self.noon_session_list = []
