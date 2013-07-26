from datetime import datetime
from pytz import timezone

class Watch():
    def get_time(self, tz_name):
        tz = timezone(tz_name)
        return tz.localize(datetime.now())

class Man():
    watch = None
    def __init__(self):
        self.watch = Watch()

    def tell_time(self):
        return 'It is now ' + self.watch.get_time('America/Chicago').strftime('%I:%M %p')
