import math

from datetime import datetime

class TimeChecker:
    def __init__(self,target_h:int,target_m:int,target_s:int,target_ms:0):
        self.chat_time = datetime.now().replace(hour=target_h,minute=target_m,second=target_s,microsecond=target_ms)

    def __getattr__(self,variable):
        if variable == "timeleft_till_next_reminder":
            return ((self.chat_time - datetime.now()).total_seconds()) - 30

fifteen_mins_before = TimeChecker(19,45,0,0)
afternoon_reminder = TimeChecker(12,30,0,0)
one_hour_before = TimeChecker(19,0,0,0)
meet_reminder = TimeChecker(19,58,0,0)

