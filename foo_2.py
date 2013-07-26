from datetime import datetime

class Watch():
    def time(self): # API Changed
        return datetime.now()

class Man():
    watch = None
    def __init__(self):
        self.watch = Watch()

    def tell_time(self):
        return 'It is now ' + self.watch.get_time().strftime('%I:%M %p') # No update here!
