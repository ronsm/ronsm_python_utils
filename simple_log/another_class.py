class AnotherClass:
    def __init__(self, sl):
        self.sl = sl
        self.sl.log_normal('another class says hello')
        self.sl.log_state(0)