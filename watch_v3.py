from datetime import datetime
from pytz import timezone

class Watch():
    def time(self, tz_name): # New required param, a timezone
        tz = timezone(tz_name)
        return tz.localize(datetime.now())
