import math

from datetime import datetime

class TimeChecker:
    def __init__(self,target_h:int,target_m:int,target_s:int,target_ms:0):
        self.chat_time = datetime.now().replace(hour=target_h,minute=target_m,second=target_s,microsecond=target_ms)
        self.timeleft_till_next_reminder = ((self.chat_time - datetime.now()).total_seconds()) - 30

thirty_mins_before = TimeChecker(19,30,0,0)
fifteen_mins_before = TimeChecker(19,45,0,0)
meet_reminder = TimeChecker(20,0,0,0)