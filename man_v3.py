from watch_v3 import Watch

class Man():
    watch = None
    def __init__(self):
        self.watch = Watch()

    def tell_time(self):
        return 'It is now ' + self.watch.time('America/Chicago').strftime('%I:%M %p')
