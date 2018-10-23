class StationSetting:
    def __init__(self, interval=0, addr=0, len=0):
        self.interval = interval
        self.holding_register_addr = addr
        self.holding_register_len = len
