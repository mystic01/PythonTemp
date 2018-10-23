
class ModbusSerialDispatcher:
    def __init__(self):
        self.sender = None

    def cycle_send(self):
        self.sender.read_holding_registers(200, 10, unit=0x1)
        self.sender.read_holding_registers(300, 20, unit=0x1)


class SettingFileReader:
    def Read(self, station_number):
        return


class StationSetting:
    def __init__(self, interval=0, addr=0, len=0):
        self.interval = interval
        self.holding_register_addr = addr
        self.holding_register_len = len
